import pytest

from accuralai_core import CoreOrchestrator, GenerateRequest


@pytest.mark.anyio("asyncio")
async def test_generate_with_default_mock_backend():
    orchestrator = CoreOrchestrator()
    try:
        request = GenerateRequest(prompt="  hello   world  ", tags=["Example"])
        response = await orchestrator.generate(request)
    finally:
        await orchestrator.aclose()

    assert response.request_id == request.id
    assert "hello world" in response.output_text
    assert response.finish_reason == "stop"
