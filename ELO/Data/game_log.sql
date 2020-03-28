Use runningball;
SELECT dateTime, League.name as League, statValueHome as home_goals, statValueForeign AS away_goals, Team.name AS home_team, Team2.name AS away_team
FROM (SportsTickerStatistics 
JOIN SportsTicker On SportsTickerStatistics.SportsTickerID = SportsTicker.IDSportsTicker) 
JOIN Team ON SportsTicker.HomeTeamID = Team.IDTeam  
JOIN Team as Team2 ON SportsTicker.ForeignTeamID = Team2.IDTeam  
JOIN League ON League.IDleague = SportsTicker.LeagueID 
WHERE LeagueID IN (136, 64, 130, 76, 146) AND SportsTickerStatisticsValueID = 0;