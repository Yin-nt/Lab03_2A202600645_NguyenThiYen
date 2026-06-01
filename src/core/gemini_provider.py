import os
import time
from typing import Any, Dict, Generator, Optional

from google import genai
from google.genai import types

from src.core.llm_provider import LLMProvider

class GeminiProvider(LLMProvider):
    def __init__(self, model_name: str = "gemini-2.5-flash", api_key: Optional[str] = None):
        super().__init__(model_name, api_key)
        resolved_api_key = self.api_key or os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=resolved_api_key)

    @staticmethod
    def _build_config(system_prompt: Optional[str] = None) -> types.GenerateContentConfig:
        config_kwargs: Dict[str, Any] = {}
        if system_prompt:
            config_kwargs["system_instruction"] = system_prompt
        return types.GenerateContentConfig(**config_kwargs)

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> Dict[str, Any]:
        start_time = time.time()
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=self._build_config(system_prompt),
        )

        end_time = time.time()
        latency_ms = int((end_time - start_time) * 1000)

        content = response.text
        usage_metadata = response.usage_metadata
        usage = {
            "prompt_tokens": getattr(usage_metadata, "prompt_token_count", 0) if usage_metadata else 0,
            "completion_tokens": getattr(usage_metadata, "response_token_count", 0) if usage_metadata else 0,
            "total_tokens": getattr(usage_metadata, "total_token_count", 0) if usage_metadata else 0,
        }

        return {
            "content": content,
            "usage": usage,
            "latency_ms": latency_ms,
            "provider": "gemini",
        }

    def stream(self, prompt: str, system_prompt: Optional[str] = None) -> Generator[str, None, None]:
        response = self.client.models.generate_content_stream(
            model=self.model_name,
            contents=prompt,
            config=self._build_config(system_prompt),
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
