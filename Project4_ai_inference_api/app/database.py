from typing import Dict, List

# Fake user database
users_db: Dict[int, dict] = {}
next_user_id = 1

# Fake prediction history database
prediction_history_db: List[dict] = []
next_prediction_id = 1