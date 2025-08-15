# TreatyWeb

A repository of NationStates Gameplay treaties, with an associated Python script to generate a network graph.

## Data Structure

An index of all indexed regions and alliances/multilateral treaties is stored in the `index.csv` file.

This file has the following structure:

- **Row 1 (Required): Entity Name**
    Pretty self-explanatory: the name of the region, alliance, or treaty. Each "entity" is represented as one separate node in the treaty network.
- **Row 2 (Required): Entity Type**
    The type of the region, alliance or treaty. One of the following:
    - **Game-Created Region**
    - **Frontier**
    - **Stronghold**
    - **Regional Union**: Several regions that behave as one single entity in terms of Foreign Affairs. The most prominent example would be The League and Concord.
    - **Alliance**: An alliance or multilateral treaty.
- **Row 3 (Optional): Treaty Index Filename**
    If the entity has a list of treaties under `data/`, the filename of its treaty index there.

## Treaty Index Structure

A list of all treaties for a specific region or entity, stored in a CSV file under `data/`.

- **Row 1: Treaty Name**
- **Row 2: Treaty Partner**

## Contributing

Any contributions to this repository are welcome! If, while adding a treaty index for a region that doesn't yet have one, you run into a treaty partner that isn't yet listed in `index.csv`, please add it there as well!

If a region isn't listed in `index.csv`, it's because I started from a few regions (GCRs, to be specific) and incrementally added their treaty partners, therefore it just means the region doesn't have a treaty with any of the currently indexed regions.