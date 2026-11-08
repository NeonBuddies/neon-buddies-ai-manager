
import random
import json
from datetime import datetime
from pathlib import Path

PROJECT = "NEON BUDDIES"
ACCOUNT = "@BusinessGry"

AGENTS = {
    "CONTENT": [
        "Meet the Neon Buddies! Unique digital collectibles with a neon identity. 💜",
        "Discover the world of Neon Buddies. Which character is your favourite? ⚡",
        "New day, new energy! Explore the Neon Buddies collection. 🚀"
    ],
    "COMMUNITY": [
        "Which Neon Buddies character would you add to your collection?",
        "Are you part of the Neon Buddies community? 💜"
    ],
    "PARTNERSHIPS": [
        "We are open to collaborations with NFT creators and Web3 communities. 🤝",
        "Looking for NFT community partnerships. Let's build together! 🚀"
    ],
    "PROMOTION": [
        "Explore Neon Buddies and discover our collection!",
        "Share the Neon Buddies universe with your NFT friends. ⚡"
    ],
    "ANALYST": [
        "Review your latest post performance and identify what works best.",
        "Track followers, engagement and collection visits."
    ]
}

def generate_daily_plan():
    today = datetime.now().strftime("%Y-%m-%d")

    plan = {
        "project": PROJECT,
        "account": ACCOUNT,
        "date": today,
        "agents": {}
    }

    for agent, ideas in AGENTS.items():
        plan["agents"][agent] = random.choice(ideas)

    Path("daily_plan.json").write_text(
        json.dumps(plan, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    post = plan["agents"]["CONTENT"] + "\n\n#NFT #Web3 #NeonBuddies"

    Path("post.txt").write_text(post, encoding="utf-8")

    print("NEON BUDDIES AI MANAGER")
    print("Daily plan generated!")
    print("\nPOST TO PUBLISH:\n")
    print(post)

if __name__ == "__main__":
    generate_daily_plan()

