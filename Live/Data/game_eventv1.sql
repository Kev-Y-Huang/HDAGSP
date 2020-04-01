USE runningball;
SELECT SportsTickerEvent.SportsTickerID, Team.name AS home_team,  Team2.name AS away_team, EventCode.description,
SportsTickerEvent.timestamp, SportsTickerEvent.min FROM SportsTickerEvent
JOIN EventCode ON SportsTickerEvent.EventCodeID = EventCode.IDEventCode
JOIN SportsTicker On SportsTickerEvent.SportsTickerID = SportsTicker.IDSportsTicker
JOIN SportsTickerStatistics On SportsTickerStatistics.SportsTickerID = SportsTicker.IDSportsTicker
JOIN Team ON SportsTicker.HomeTeamID = Team.IDTeam  
JOIN Team as Team2 ON SportsTicker.ForeignTeamID = Team2.IDTeam  
JOIN League ON League.IDleague = SportsTicker.LeagueID 
WHERE LeagueID IN (136, 64, 130, 76, 146) AND SportsTickerStatisticsValueID = 0;