import argparse

from agents import BrowserAgent
from browsers import PlaywrightComputer


PLAYWRIGHT_SCREEN_SIZE = (1440, 900)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the browser agent with a query.")
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="The query for the browser agent to execute.",
    )

    parser.add_argument(
        "--initial_url",
        type=str,
        default="https://www.google.com",
        help="The inital URL loaded for the computer.",
    )
    
    parser.add_argument(
        "--model",
        default='gemini-2.5-computer-use-preview-10-2025',
        help="Set which main model to use.",
    )

    args = parser.parse_args()

    env = PlaywrightComputer(
        screen_size=PLAYWRIGHT_SCREEN_SIZE,
        initial_url=args.initial_url,
        highlight_mouse=False,
    )

    with env as browser_computer:
        agent = BrowserAgent(
            browser_computer=browser_computer,
            query=args.query,
            model_name=args.model,
        )
        agent.agent_loop()
    agent.agent_loop()
    
    return 0


if __name__ == "__main__":
    main()