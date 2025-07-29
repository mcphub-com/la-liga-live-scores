import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/heisenbug/api/la-liga-live-scores'

mcp = FastMCP('la-liga-live-scores')

@mcp.tool()
def team(name: Annotated[str, Field(description='')]) -> dict: 
    '''Returns info about the team'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/team'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venue(name: Annotated[str, Field(description='')]) -> dict: 
    '''Returns venue data'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/venue'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def referees_statistics() -> dict: 
    '''Referees statistics'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/table/referee'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_statistics(team1: Annotated[str, Field(description='Home team name')],
                     team2: Annotated[str, Field(description='Away team name')],
                     live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Returns match statistics'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/match/stats'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_scorers(team1: Annotated[str, Field(description='Home team name')],
                  team2: Annotated[str, Field(description='Away team name')],
                  live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return scorers for a match'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/scorers'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_table(fromdate: Annotated[Union[str, None], Field(description='Compute the table only with matches played fromdate (format mmddyyyy)')] = None,
                 todate: Annotated[Union[str, None], Field(description='Compute the tables only with matches played todate (format mmddyyyy)')] = None,
                 to: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the last match number to consider to compute the table (default last match number played registered on system)')] = None,
                 _from: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the first match number to use to compute the table (default 1)')] = None,
                 time: Annotated[Union[str, None], Field(description='Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).')] = None,
                 season: Annotated[Union[str, None], Field(description='Season code (default 2016-17)')] = None,
                 mode: Annotated[Union[str, None], Field(description='Optional parameter to restrict the table compute on home or away games (default all)')] = None) -> dict: 
    '''Return current league table'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/table'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fromdate': fromdate,
        'todate': todate,
        'to': to,
        'from': _from,
        'time': time,
        'season': season,
        'mode': mode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_scorers(how: Annotated[Union[str, None], Field(description='Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.')] = None,
                fromdate: Annotated[Union[str, None], Field(description='Compute the table only with matches played fromdate (format mmddyyyy)')] = None,
                todate: Annotated[Union[str, None], Field(description='Compute the table only with matches played todate (format mmddyyyy)')] = None,
                page: Annotated[Union[int, float, None], Field(description='Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).')] = None,
                to: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)')] = None,
                mode: Annotated[Union[str, None], Field(description='Optional parameter to restrict the table compute on home or away games (default all)')] = None,
                player: Annotated[Union[str, None], Field(description='Optional parameter to get goals number only for the player name specified')] = None,
                team: Annotated[Union[str, None], Field(description='Team name')] = None,
                _from: Annotated[Union[int, float, None], Field(description='Optional parameter to specify the first match number to use to compute the result (default 1)')] = None) -> dict: 
    '''Returns top scorers for the league'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/table/scorers'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'how': how,
        'fromdate': fromdate,
        'todate': todate,
        'page': page,
        'to': to,
        'mode': mode,
        'player': player,
        'team': team,
        'from': _from,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_stats_for_amatch(player: Annotated[str, Field(description='Player name')],
                            team1: Annotated[str, Field(description='Home team name')],
                            team2: Annotated[str, Field(description='Away team name')],
                            live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return the player's statistics for a match'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/match/player'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_details(player: Annotated[str, Field(description='Player name')],
                   team: Annotated[str, Field(description='Team name')],
                   honours: Annotated[Union[bool, None], Field(description='Return only the honours for the player (default false)')] = None) -> dict: 
    '''Returns all data about a player. Available only with ULTRA and MEGA plans!'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/playerdetails'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'team': team,
        'honours': honours,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lineups_and_substitutes_for_agame(team1: Annotated[str, Field(description='Home team name')],
                                      team2: Annotated[str, Field(description='Away team name')],
                                      live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Return lineups, substitutes and coaches for a game.'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/formations'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_events(team1: Annotated[str, Field(description='Home team name')],
                 team2: Annotated[str, Field(description='Away team name')],
                 live: Annotated[Union[bool, None], Field(description='Returns data for a playing match (default false)')] = None) -> dict: 
    '''Returns events l(yellow and red cards, substitutions, missing penalties and formation module...) for a match'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/match/events'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def season_matches_results(team1: Annotated[Union[str, None], Field(description='Returns all matches with team1')] = None,
                           team2: Annotated[Union[str, None], Field(description='Return all matches with team2')] = None,
                           date: Annotated[Union[str, None], Field(description='Returns all matches for the date (format mmddyyyy)')] = None,
                           season: Annotated[Union[str, None], Field(description='Season code (default 2016-17)')] = None,
                           matchday: Annotated[Union[str, None], Field(description='Return all the games results for the match day specified.')] = None,
                           live: Annotated[Union[bool, None], Field(description='Returns results for playing matches (live) (default false). Overwrite all the others parameters.')] = None) -> dict: 
    '''Return Season matches results'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
        'date': date,
        'season': season,
        'matchday': matchday,
        'live': live,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_players(team: Annotated[str, Field(description='Team name')]) -> dict: 
    '''Returns all players for a team'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/players'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def missing_players_for_amatch(team1: Annotated[str, Field(description='Home team name')],
                               team2: Annotated[str, Field(description='Away team name')]) -> dict: 
    '''Return missing players for a match'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/match/missing'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team1': team1,
        'team2': team2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def prediction(team2: Annotated[str, Field(description='Away team name')],
               team1: Annotated[str, Field(description='Home team name')]) -> dict: 
    '''Returns match result perdiction (use an AI deep learning engine)'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/predict'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team2': team2,
        'team1': team1,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bookmakers_list(team2: Annotated[str, Field(description='Away Team')],
                    team1: Annotated[str, Field(description='Home team')]) -> dict: 
    '''Return the list of the available bookmakers for a match'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/listbookmakers'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team2': team2,
        'team1': team1,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def odds_list(team2: Annotated[str, Field(description='Away team')],
              team1: Annotated[str, Field(description='Home team')],
              bookmaker: Annotated[str, Field(description='Bookmaker name')]) -> dict: 
    '''Returns the available odds for a match and a bookmaker'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/listodds'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team2': team2,
        'team1': team1,
        'bookmaker': bookmaker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def odd_quotas(team2: Annotated[str, Field(description='Away team')],
               team1: Annotated[str, Field(description='Home team')],
               odd: Annotated[str, Field(description='Odd name')],
               bookmaker: Annotated[str, Field(description='Bookmaker name')]) -> dict: 
    '''Returns quotas for an odd a match and a bookmaker'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/odds'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team2': team2,
        'team1': team1,
        'odd': odd,
        'bookmaker': bookmaker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet_stats(bet: Annotated[str, Field(description='Type of data required, result, totalgoals,underover,1x2,goalnogoal')],
              fromdate: Annotated[Union[str, None], Field(description='Only matches fromdate (format mmddyyyy)')] = None,
              handicap: Annotated[Union[int, float, None], Field(description='Handicap values (only for 1x2 bet)')] = None,
              mode: Annotated[Union[str, None], Field(description='Together with team parameter, let you to select only games where team has played home, away or all (default)')] = None,
              team: Annotated[Union[str, None], Field(description='Team name')] = None,
              time: Annotated[Union[str, None], Field(description='Let you to select only first half (FH) result, second half (SH) or full time (FT) default')] = None,
              todate: Annotated[Union[str, None], Field(description='Only matches todate (format mmddyyyy)')] = None,
              when: Annotated[Union[str, None], Field(description='Let you to select only games with win, loss, draw or all (default)')] = None,
              over: Annotated[Union[int, float, None], Field(description='Over values limit, mandatory for underover bet')] = None) -> dict: 
    '''Returns aggregate data about results, goal-nogoal, underover, 1x2 and totalgoals to support your bet activities'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/table/betting'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bet': bet,
        'fromdate': fromdate,
        'handicap': handicap,
        'mode': mode,
        'team': team,
        'time': time,
        'todate': todate,
        'when': when,
        'over': over,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def activate_webhook(token: Annotated[str, Field(description='Token')]) -> dict: 
    '''Activate a webhook registered with the subscribe endpoint. Not available for BASIC plan.'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/push/activate'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'token': token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_subscribed() -> dict: 
    '''Returns all the events subscribed. Not available for BASIC plan.'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/push/lis'
    headers = {'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def subscribe(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Register to an event for push notifications. Not available for BASIC plan.'''
    url = 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/push/subscribe'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'heisenbug-la-liga-live-scores-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
