from flatland.envs.rail_env_utils import load_flatland_environment_from_file


env = load_flatland_environment_from_file("Level_0.pkl")

local_observation, info = env.reset(
    regenerate_rail=True,
    regenerate_schedule=True,
    activate_agents=False,
    random_seed=3838
)

pass