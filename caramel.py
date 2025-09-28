"""
Caramel: Contextual Multi-Agent Orchestrator
"""

from redis import Redis
# from qdrant_client import QdrantClient

class CaramelOrchestrator:
    def __init__(self, redis_url="redis://localhost:6379/0"):
        self.redis = Redis.from_url(redis_url)
        # self.vector = QdrantClient("http://localhost:6333")

    def analyze(self, message: str) -> dict:
        """
        Pinned analysis agent: classify intent, topic, granularity.
        Returns a dict stub for now.
        """
        return {
            "topic": "default",
            "granularity": "L0",
            "needs": {}
        }

    def route(self, message: str) -> str:
        """
        Routes message to the appropriate agent (stub).
        """
        analysis = self.analyze(message)
        # TODO: fetch corpus, call agent
        return f"[CaramelOrchestrator] Routed '{message}' with analysis {analysis}"


if __name__ == "__main__":
    orch = CaramelOrchestrator()
    print(orch.route("Hello Caramel"))
