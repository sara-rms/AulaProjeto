#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1':
                list_bg = []
                for i in range(1,9):
                    list_bg.append(Background(name=f'Level1-{i}', position=(0, 0)))
                return list_bg

    pass
