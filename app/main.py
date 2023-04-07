import os

import click
import uvicorn

from intra import ic

@click.command()
@click.option(
  "--env",
  type=click.Choice(["dev", "prod"], case_sensitive=False),
  default="dev",
)

@click.option(
  "--debug",
  type=click.BOOL,
  is_flag=True,
  default=False
)
def main(env, debug):
    os.environ['ENV'] = env
    os.environ['DEBUG'] = str(debug)

    user = ic.get('users/jgengo').json()

    uvicorn.run(
        app="server:app",
        host='0.0.0.0',
        port=8000,
        reload=True if os.environ['ENV'] != "prod" else False,
        workers=1,
    )

if __name__ == "__main__":
    main()