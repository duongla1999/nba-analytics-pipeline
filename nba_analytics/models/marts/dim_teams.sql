with team_histories as (
    select * from {{ ref('stg_team_histories') }}
),
ranked as (
    select
        *,
        row_number() over (partition by team_id order by season_active_till desc) as rn
    from team_histories
)
select
    team_id,
    team_name,
    team_city,
    team_abbrev,
    season_founded,
    season_active_till,
    league
from ranked
where rn = 1