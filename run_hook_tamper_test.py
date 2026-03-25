import json
from pathlib import Path

from backend.app.services.simulation_runner import SimulationRunner


class DummyState:
    simulation_id = "test"
    twitter_current_round = 0
    reddit_current_round = 0
    twitter_simulated_hours = 0
    reddit_simulated_hours = 0
    current_round = 0
    simulated_hours = 0
    twitter_completed = False
    reddit_completed = False
    twitter_running = True
    reddit_running = False
    twitter_actions_count = 0
    reddit_actions_count = 0

    def add_action(self, action):
        print("[ACTION PROCESSED]", action.action_type)


log_dir = Path("/root/mirofish/test_logs/twitter")
log_dir.mkdir(parents=True, exist_ok=True)
log_path = log_dir / "actions.jsonl"

payload = {
    "round": 1,
    "timestamp": "2026-01-01T00:00:00",
    "agent_id": 1,
    "agent_name": "agent_alpha",
    "action_type": "CREATE_POST",
    "action_args": {"content": "Hello world"},
    "result": "ok",
    "success": True,
}

with open(log_path, "w", encoding="utf-8") as f:
    f.write(json.dumps(payload) + "\n")

state = DummyState()

print("1) VALID LOG")
SimulationRunner._read_action_log(
    str(log_path),
    0,
    state,
    "twitter",
)

# second pass with same file = replay in the same runtime path
print("\n2) REPLAY SAME LOG")
SimulationRunner._read_action_log(
    str(log_path),
    0,
    state,
    "twitter",
)
