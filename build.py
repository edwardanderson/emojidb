'''
Build a core Linked Art representation from the canonical Unicode data.
'''


import json
from pathlib import Path


def group_name(s):
    return s.split(':')[-1].strip()


sets = dict()

with open('notes/emoji-test.txt', 'r') as in_file:
    for line in in_file:
        if line == '\n':
            continue
        else:
            row = line.strip()

        if row.startswith('#'):
            if row.startswith('# group'):
                group = group_name(row)
                sets[group] = set()
                subgroup = None
            elif row.startswith('# subgroup'):
                subgroup = group_name(row)
                sets[group].add(subgroup)
            else:
                # Comment.
                continue
        else:
            shortcode, qualifier_description = row.split(';')
            qualifier, version_label = qualifier_description.split('#', 1)
            emoji, version_label = version_label.split('E', 1)
            version, label = version_label.split(' ', 1)
            subgroup_id = subgroup.replace(' ', '-').lower()
            emoji = emoji.strip()
            label = label.replace('’', "'")

            document = {
                '@context': 'https://linked.art/ns/v1/linked-art.json',
                'id': f'https://www.emojidb.art/{emoji}',
                'type': 'Mark',
                '_label': label,
                'classified_as': {
                    'id': 'http://vocab.getty.edu/aat/300412189',
                    'type': 'Type',
                    '_label': 'Emoji'
                },
                'identified_by': [
                    {
                        'type': 'Name',
                        'content': ' '.join([i.capitalize() for i in label.split()]),
                        'classified_as': {
                            'id': 'http://vocab.getty.edu/aat/300404670',
                            'type': 'Type',
                            '_label': 'Primary Name'
                        },
                        'language': {
                            'id': 'http://vocab.getty.edu/aat/300388277',
                            'type': 'Language',
                            '_label': 'English'
                        }
                    },
                    {
                        'id': f'https://www.emojidb.art/identifier/{emoji}',
                        'type': 'Identifier',
                        'content': emoji
                    }
                ],
                'member_of': {
                    'id': f'https://www.emojidb.art/set/{subgroup_id}',
                    'type': 'Set',
                    '_label': subgroup
                }
            }

            # Identifier parts.
            identifier_parts = [item for item in emoji if item]
            if len(identifier_parts) > 1:
                # print(emoji, identifier_parts)
                if len(identifier_parts) == 2 and identifier_parts[1] == '‍':
                    pass
                else:
                    document['identified_by'][-1]['part'] = list()
                    for identifier in identifier_parts:
                        document['identified_by'][-1]['part'].append(
                            {
                                'id': f'https://www.emojidb.art/identifier/{identifier}',
                                'type': 'Identifier',
                                'content': identifier
                            }
                        )

            out_path = Path(f'data/mark/{emoji}').mkdir(parents=True, exist_ok=True)
            with open(f'data/mark/{emoji}/index.json', 'w') as out_file:
                json.dump(document, out_file, indent=2, ensure_ascii=False)

# Groups.
for key in sets:
    group_id = key.replace(' ', '_').lower()
    group = {
        '@context': 'https://linked.art/ns/v1/linked-art.json',
        'id': f'https://www.emojidb.art/set/{group_id}',
        'type': 'Set',
        '_label': key,
        'identified_by': {
            'type': 'Name',
            'content': key,
            'classified_as': {
                'id': 'http://vocab.getty.edu/aat/300404670',
                'type': 'Type',
                '_label': 'Primary Name'
            },
            'language': {
                'id': 'http://vocab.getty.edu/aat/300388277',
                'type': 'Language',
                '_label': 'English'
            }
        }
    }
    with open(f'data/set/{group_id}.json', 'w') as out_file:
        json.dump(group, out_file, indent=2, ensure_ascii=False)
 
    subgroups = sets[key]
    for item in subgroups:
        subgroup_id = item.replace(' ', '_').lower()
        subgroup = {
            '@context': 'https://linked.art/ns/v1/linked-art.json',
            'id': f'https://www.emojidb.art/set/{subgroup_id}',
            'type': 'Set',
            '_label': item,
            'identified_by': {
                'type': 'Name',
                'content': item.replace('-', ' ').title(),
                'classified_as': {
                    'id': 'http://vocab.getty.edu/aat/300404670',
                    'type': 'Type',
                    '_label': 'Primary Name'
                },
                'language': {
                    'id': 'http://vocab.getty.edu/aat/300388277',
                    'type': 'Language',
                    '_label': 'English'
                }
            },
            'member_of': {
                'id': f'https://www.emojidb.art/set/{group_id}',
                'type': 'Set',
                '_label': key
            }
        }
        with open(f'data/set/{subgroup_id}.json', 'w') as out_file:
            json.dump(subgroup, out_file, indent=2, ensure_ascii=False)
    