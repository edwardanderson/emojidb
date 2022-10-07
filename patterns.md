# Patterns

- [Patterns](#patterns)
  - [Core](#core)
  - [Group](#group)
  - [Name](#name)
    - [Multiple Languages](#multiple-languages)
  - [Identifier](#identifier)
    - [Identifier Part](#identifier-part)
  - [Representation](#representation)
    - [Instance Type](#instance-type)
    - [Instance](#instance)
  - [Colour](#colour)
  - [Part](#part)
  - [Equivalent](#equivalent)

## Core

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    }
}
```

## Group

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "member_of": {
        "id": "https://unicode.org/emoji/charts/full-emoji-list.html#food-fruit",
        "type": "Set",
        "_label": "food-fruit",
        "member_of": {
            "id": "https://unicode.org/emoji/charts/full-emoji-list.html#food_&_drink",
            "type": "Set",
            "_label": "Food & Drink"
        }
    }
}
```

## Name

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "identified_by": {
        "type": "Name",
        "content": "Red Apple",
        "language": {
            "id": "http://vocab.getty.edu/aat/300388277",
            "type": "Language",
            "_label": "English"
        }
    }
}
```

### Multiple Languages

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "identified_by": [
        {
            "type": "Name",
            "content": "Red Apple",
            "language": {
                "id": "http://vocab.getty.edu/aat/300388277",
                "type": "Language",
                "_label": "English"
            }
        },
        {
            "type": "Name",
            "content": "Pomme Rouge",
            "language": {
                "id": "http://vocab.getty.edu/aat/300388306",
                "type": "Language",
                "_label": "French"
            }
        }
    ]
}
```

## Identifier

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "identified_by": [
        {
            "id": "https://www.emojidb.art/identifier/🍎",
            "type": "Identifier",
            "content": "🍎"
        },
        {
            "type": "Identifier",
            "content": "1F469 200D 1F680",
            "classified_as": {
                "id": "http://www.wikidata.org/entity/Q109615047",
                "type": "Type",
                "_label": "Unicode code point"
            }
        },
        {
            "type": "Identifier",
            "content": ":apple:",
            "classified_as": {
                "id": "http://www.wikidata.org/entity/Q114228968",
                "type": "Type",
                "_label": "Shortcode"
            }
        }
    ]
}
```

### Identifier Part

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/👩‍🚀",
    "type": "Mark",
    "_label": "Woman Astronaut",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "identified_by": [
        {
            "id": "https://www.emojidb.art/identifier/👩‍🚀",
            "type": "Identifier",
            "content": "👩‍🚀",
            "_label": "Woman Astronaut",
            "part": [
                {
                    "id": "https://www.emojidb.art/identifier/👩",
                    "type": "Identifier",
                    "content": "👩",
                    "_label": "Woman"
                },
                {
                    "id": "https://www.emojidb.art/identifier/🚀",
                    "type": "Identifier",
                    "content": "🚀",
                    "_label": "Rocket"
                }
            ]
        }
    ]
}
```

## Representation

### Instance Type

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "represents_instance_of_type": {
        "id": "http://vocab.getty.edu/aat/300266417",
        "type": "Type",
        "_label": "apples (fruits)"
    }
}
```

### Instance

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🇫🇷",
    "type": "Mark",
    "_label": "Flag: France",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "represents": {
        "id": "http://www.wikidata.org/entity/Q43192",
        "type": "InformationObject",
        "_label": "flag of France"
    }
}
```

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🗼",
    "type": "Mark",
    "_label": "Tokyo Tower",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "represents": {
        "id": "http://www.wikidata.org/entity/Q183536",
        "type": "HumanMadeObject",
        "_label": "Tokyo Tower"
    }
}
```

## Colour

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "digitally_shown_by": {
        "type": "Digital Object",
        "dimension": {
            "type": "Dimension",
            "classified_as": [
                {
                    "id": "http://vocab.getty.edu/aat/300080438",
                    "type": "Type",
                    "_label": "Colour"
                },
                {
                    "id": "http://vocab.getty.edu/aat/300126225",
                    "type": "Type",
                    "_label": "Red"
                }
            ]
        }
    }
}
```

## Part

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/👩‍🚀",
    "type": "Mark",
    "_label": "Woman Astronaut",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "part": [
        {
            "id": "https://www.emojidb.art/🧑‍🚀",
            "type": "Mark",
            "_label": "Astronaut"
        },
        {
            "id": "https://www.emojidb.art/👩",
            "type": "Mark",
            "_label": "Woman"
        }
    ]
}
```

## Equivalent

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json",
    "id": "https://www.emojidb.art/🍎",
    "type": "Mark",
    "_label": "Red Apple",
    "classified_as": {
        "id": "http://vocab.getty.edu/aat/300412189",
        "type": "Type",
        "_label": "Emoji"
    },
    "equivalent": [
        {
            "id": "https://unicode.org/emoji/charts/full-emoji-list.html#1f34e",
            "type": "Mark",
            "_label": "red apple"
        },
        {
            "id": "http://📙.la/🍎",
            "type": "Mark",
            "_label": "red apple"
        }
    ]
}
```
