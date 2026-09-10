with source as (
    select * from {{ source ('nba', 'games') }}
),

renamed as (
    select
        "gameId" as game_id,
        "gameDate" as game_date,
        "hometeamId" as home_team_id,
        "awayteamId" as away_team_id,
        "hometeamName" as home_team_name,
        "awayteamName" as away_team_name,
        "homeScore" as home_score,
        "awayScore" as away_score,
        "gameType" as game_type
    from source
)

select * from renamed