with players as (
    select * from {{ ref('stg_players') }}
)

select
    player_id,
    first_name,
    last_name,
    birth_date,
    country,
    height_inches,
    body_weight_lbs,
    guard,
    forward,
    center,
    draft_year,
    draft_round,
    draft_number,
    from_year,
    to_year
from players