# TrustHandoff × MiroFish Demo

> Hooks into MiroFish `simulation_runner._read_action_log` (action ingestion boundary)

Minimal proof-of-concept showing TrustHandoff attached to a real MiroFish runtime.

This demo instruments MiroFish's action log processing path and shows:

- valid action → accepted
- replayed action → rejected

## Run

```bash
python run_hook_tamper_test.py
```

## Expected output

```text
1) VALID LOG
[ACCEPT] twitter agent=1 action=CREATE_POST
[ACTION PROCESSED] CREATE_POST

2) REPLAY SAME LOG
[REJECT] replay detected
```

## Scope

This is not a full MiroFish integration.

It demonstrates one concrete trust boundary:
action log ingestion.
