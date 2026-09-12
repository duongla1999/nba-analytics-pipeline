with team_stats as (
    select * from {{ ref('stg_team_statistics') }}
)

select * from team_stats