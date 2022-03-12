onlygrass = ['Soil','Soil/Grass']
layer4 = {
    'None': {
        'prev': [],
        'prob': 4990/9990,
        'file': ''
    },
    'Roots': {
        'prev': [],
        'prob': 2000/9990,
        'file': 'layer4/Roots.png'
    },
    'Roots/Micelium': {
        'prev': onlygrass,
        'prob': 1500/9990,
        'file': 'layer4/Roots Micelium.png'
    },
    'Roots/Worms': {
        'prev': onlygrass,
        'prob': 1400/9990,
        'file': 'layer4/Roots Worms.png'
    },
    'Roots/Micelium/worms': {
        'prev': onlygrass,
        'prob': 100/9990,
        'selection': True,
        'file': 'layer4/Roots Worms Micelium.png'    
    }
}