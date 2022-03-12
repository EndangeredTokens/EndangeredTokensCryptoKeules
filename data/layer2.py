day = ['Light Blue', 'Orange', 'Purple', 'Grey', 'Red', 'Yellow', 'Blue']
night = ['Black']
layer2 = {
    'Sun': {
        'prev': night,
        'prob': 1340/9990,
        'file': 'layer2/Sun.png'
    },
    'Rainbow': {
        'prev': night,
        'prob': 200/9990,
        'selection': True,       
        'file': 'layer2/Rainbow.png'
    },
    'Sun/Rainbow': {
        'prev': night,
        'prob': 200/9990,
        'selection': True,
        'file': 'layer2/Rainbow Sun.png'
    },
    'Sun/Clouds': {
        'prev': night,
        'prob': 2000/9990,
        'file': 'layer2/Sun Clouds.png'
    },
    'Rainbow/Ufo': {
        'prev': night,
        'prob': 100/9990,
        'selection': True,
        'file': 'layer2/Rainbow UFO.png'
    },
    'Clouds/Rainbow': {
        'prev': night,
        'prob': 100/9990,
        'selection': True,
        'file': 'layer2/Clouds Rainbow.png'
    },
    'Clouds/Cloud/Sun': {
        'prev': night,
        'prob': 1000/9990,
        'file': 'layer2/Clouds Cloud Sun.png'
    },
    'Clouds/Cloud/Rainbow': {
        'prev': night,
        'prob': 200/9990,
        'selection': True,
        'file': 'layer2/Clouds Cloud Rainbow.png'
    },
    'Clouds/Cloud/Rainbow/Sun': {
        'prev': night,
        'prob': 100/9990,
        'selection': True,
        'file': 'layer2/Clouds Cloud Rainbow Sun.png'
    },
    'Clouds/Rainbow/UFO': {
        'prev': night,
        'prob': 100/9990,
        'selection': True,
        'file': 'layer2/Clouds Rainbow UFO.png'
    },
    'Clouds': {
        'prev': [],
        'prob': 1000/9990,
        'file': 'layer2/Clouds.png'
    },
    'Clouds/UFO': {
        'prev': [],
        'prob': 100/9990,
        'selection': True,
        'file': 'layer2/Clouds UFO.png'
    },
    'Clouds/Cloud': {
        'prev': [],
        'prob': 1000/9990,
        'file': 'layer2/Clouds Cloud.png'
    },
    'Clouds/Star': {
        'prev': [],
        'prob': 50/9990,
        'file': 'layer2/Clouds Star.png'
    },
    'Clouds/Cloud/Moon': {
        'prev': [],
        'prob': 500/9990,
        'file': 'layer2/Clouds Cloud Moon.png'
    },
    'Clouds/Moon': {
        'prev': [],
        'prob': 1000/9990,
        'file': 'layer2/Clouds Moon.png'
    },
    'None': {
        'prev': day,
        'prob': 50/9990,
        'file': ''
    },
    'Thndr/Star': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Star.png'
    },
    'Thndr/Clouds/Star': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Clouds Star.png'
    },
    'Thndr/Clouds/Moon': {
        'prev': day,
        'prob': 10/9990,
        'selection': True,
        'file': 'layer2/Thunder Clouds Moon.png'
    },
    'Thndr/Clouds/UFO': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Clouds UFO.png'
    },
    'Thndr/Clouds/Cloud': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Clouds Cloud.png'
    },
    'Thndr/Clouds/Cloud/Moon': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Clouds Cloud Moon.png'
    },
    'Thndr/Moon': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Moon.png'
    },
    'Thndr/Clouds': {
        'prev': day,
        'prob': 50/9990,
        'selection': True,
        'file': 'layer2/Thunder Clouds.png'
    },
    'Thndr/Ufo': {
        'prev': day,
        'prob': 10/9990,
        'selection': True,
        'file': 'layer2/Thunder UFO.png'
    },
    'Thndr': {
        'prev': day,
        'prob': 100/9990,
        'selection': True,
        'file': 'layer2/Thunder.png'
    },
    'Stars': {
        'prev': [],
        'prob': 100/9990,
        'file': 'layer2/Stars.png'
    },
    'Stars/Clouds/Cloud/Moon': {
        'prev': [],
        'prob': 40/9990,
        'file': 'layer2/Stars Clouds Cloud Moon.png'
    },
    'Stars/Clouds/Cloud': {
        'prev': [],
        'prob': 100/9990,
        'file': 'layer2/Stars Clouds Cloud.png'
    },
    'Stars/UFO': {
        'prev': [],
        'prob': 20/9990,
        'selection': True,
        'file': 'layer2/Stars UFO.png'
    },
    'Stars/Clouds': {
        'prev': [],
        'prob': 100/9990,
        'file': 'layer2/Stars Clouds.png'
    },
    'Stars/Clouds/Star': {
        'prev': [],
        'prob': 100/9990,
        'file': 'layer2/Stars Clouds Star.png'
    },
    'Stars/Clouds/UFO': {
        'prev': [],
        'prob': 20/9990,
        'selection': True,
        'file': 'layer2/Stars Clouds UFO.png'
    },
}
