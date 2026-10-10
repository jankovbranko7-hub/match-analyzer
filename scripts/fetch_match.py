#!/usr/bin/env python3
"""Fetch FootyStats data for match analysis.
Usage: python fetch_match.py --match "Home vs Away" [--date YYYY-MM-DD]
Or provide match_id.
Key aus der Umgebungsvariable FOOTYSTATS_KEY.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

API_KEY = os.environ.get("FOOTYSTATS_KEY", "")
BASE = "https://api.football-data-api.com"

def api_get(endpoint, params=None):
    if params is None:
        params = {}
    params["key"] = API_KEY
    url = f"{BASE}/{endpoint}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching {endpoint}: {e}", file=sys.stderr)
        return None

def find_match(home, away, date=None):
    params = {}
    if date:
        params["date"] = date
    data = api_get("todays-matches", params)
    if not data or not data.get("success"):
        return None
    matches = data.get("data", [])
    for m in matches:
        # Exact match preferred; check names
        hname = m.get("home_name") or m.get("homeName") or ""
        aname = m.get("away_name") or m.get("awayName") or ""
        if home.lower() in hname.lower() and away.lower() in aname.lower():
            return m
        # Also try reverse or exact
    # Fallback: search more carefully
    for m in matches:
        hname = (m.get("home_name") or "").lower()
        aname = (m.get("away_name") or "").lower()
        if (home.lower() in hname and away.lower() in aname) or (away.lower() in hname and home.lower() in aname):
            return m
    return None

def get_team_stats(season_id, team_id):
    data = api_get("league-teams", {"season_id": season_id, "include": "stats"})
    if not data or not data.get("success"):
        return None
    for team in data.get("data", []):
        if team.get("id") == team_id:
            return team
    return None

def get_lastx(team_id):
    data = api_get("lastx", {"team_id": team_id})
    if not data or not data.get("success"):
        return None
    # Prefer last 6
    for item in data.get("data", []):
        if item.get("last_x_match_num") == 6:
            return item
    return data.get("data", [None])[0]

def get_match_details(match_id):
    return api_get("match", {"match_id": match_id})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", required=True)
    parser.add_argument("--away", required=True)
    parser.add_argument("--date", default=None)
    parser.add_argument("--match-id", type=int, default=None)
    args = parser.parse_args()

    if args.match_id:
        match = {"id": args.match_id}
        # Need more details; fetch match
        details = get_match_details(args.match_id)
        if details and details.get("success"):
            match = details.get("data", [{}])[0] if isinstance(details.get("data"), list) else details.get("data", {})
    else:
        match = find_match(args.home, args.away, args.date)
        if not match:
            print(json.dumps({"error": "Match not found exactly. Similar names rejected."}))
            sys.exit(1)

    match_id = match.get("id")
    home_id = match.get("homeID") or match.get("home_id")
    away_id = match.get("awayID") or match.get("away_id")
    season = match.get("season")  # may need season_id from elsewhere

    # For season_id, often from league or match; assume we need to find it
    # For simplicity, if we have season, but API uses season_id integer.
    # In practice, fetch match details for full info.
    details = get_match_details(match_id)
    if details and details.get("success"):
        md = details.get("data")
        if isinstance(md, list):
            md = md[0]
        match.update(md or {})

    # Get season_id: often in competition or from teams
    # Fallback: use league-teams with known season if possible; for demo, proceed with team_ids

    home_stats = None
    away_stats = None
    # To get season_id, look in match or search leagues; simplified: assume we can get from teams endpoint if we know season
    # For real use, agent should handle finding season_id from match or league.

    result = {
        "match": match,
        "home_id": home_id,
        "away_id": away_id,
        "note": "Fetch team stats with league-teams?include=stats using correct season_id. Lastx for form."
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
