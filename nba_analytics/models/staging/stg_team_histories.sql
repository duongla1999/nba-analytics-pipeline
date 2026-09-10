with source as (
    select * from {{ source ('nba', 'teamHistories') }}
),

renamed as (
    select
        "teamId" as team_id,
        "teamCity" as team_city,
        "teamName" as team_name,
        "teamAbbrev" as team_abbrev,
        "seasonFounded" as season_founded,
        "seasonActiveTill" as season_active_till,
        "league" as league
    from source
)

select * from renamed