import json

def create_dataset_json(
    name,
    id,
    title,
    description,
    temporal_schema,
    composition_function,
    grid_ref_sys,
    collection_type,
    provider_url,
    provider_name,
    roles,
    version,
    bands_info,
    keywords,
    sources,
    license_type,
    license_uri,
    public,
    available,
    category
):
    dataset = {
        "id": id,
        "name": name,
        "title": title,
        "description": description,
        "temporal_composition_schema": temporal_schema,
        "composition_function": composition_function,
        "grid_ref_sys": grid_ref_sys,
        "collection_type": collection_type,
        "metadata": {
            "providers": [
                {
                    "url": provider_url,
                    "name": provider_name,
                    "roles": roles,
                }
            ],
            "license": {
                "type": license_type,
                "uri": license_uri
            }
        },
        "keywords": keywords,
        "is_public": public,
        "is_available": available,
        "category": category,
        "version": version,
        "version_predecessor": None,
        "version_successor": None,
        "bands": bands_info,
        "properties": {
            "sources": sources
        }
    }

    return dataset