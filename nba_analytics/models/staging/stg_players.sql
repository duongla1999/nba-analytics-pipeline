with source as (
    select * from {{ source ('nba', 'players') }}
),

renamed as (
    select
        "personId" as player_id,
        "firstName" as first_name,
        "lastName" as last_name,
        "birthDate" as birth_date,
        "country" as country,
        "heightInches" as height_inches,
        "bodyWeightLbs" as body_weight_lbs,
        "guard" as guard,
        "forward" as forward,
        "center" as center,
        "draftYear" as draft_year,
        "draftRound" as draft_round,
        "draftNumber" as draft_number,
        "fromYear" as from_year,
        "toYear" as to_year
    from source
)

select * from renamed