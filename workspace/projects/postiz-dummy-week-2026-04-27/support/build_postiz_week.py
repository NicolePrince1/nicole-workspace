from pathlib import Path
import json

out = Path('/data/.openclaw/workspace/tmp/postiz-week-2026-04-27')
out.mkdir(parents=True, exist_ok=True)

linkedin = 'cmo8gmcii05bin50ytakd9ehj'
facebook = 'cmo8gnucn05r3ld0yciyxbdpw'
x = 'cmo8gp7wo05rald0y4xqwghcq'
youtube = 'cmo8gwsbg05c0n50yglmyot7h'
video = {
    'id': '4d034a1d-6991-4ff8-853c-b7c7cd49a9cd',
    'path': 'https://uploads.postiz.com/NBPhSXTcpC.mp4'
}

week = [
    {
        'file': '2026-04-27-monday.json',
        'date': '2026-04-27T07:00:00.000Z',
        'tag': 'monday',
        'linkedin': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nIf your agency spends more time building reports than using them, the reporting stack is broken.\n\nAgencies do not need more dashboard clutter.\nThey need reporting that feels invisible, dependable, and done.\n\nThat means faster setup, cleaner delivery, fewer moving parts, and less client-facing friction.\n\nThat should be the standard.",
        'facebook': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nReporting should not feel like a second job.\n\nThe best reporting systems are the ones agencies barely need to think about because they just work, stay clean, and get delivered without drama.",
        'x': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nIf reporting feels like a second job, the stack is broken. Agencies need reporting that feels invisible, dependable, and done.",
        'youtube_title': 'DUMMY TEST - Reporting Should Not Feel Like a Second Job',
        'youtube_desc': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nThis placeholder YouTube upload supports a weekly dummy content run for Oviond.\n\nCore idea: agencies do not need more dashboard clutter. They need reporting that feels invisible, dependable, and done."
    },
    {
        'file': '2026-04-28-tuesday.json',
        'date': '2026-04-28T07:00:00.000Z',
        'tag': 'tuesday',
        'linkedin': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nA pretty dashboard does not automatically create trust.\n\nTrust comes from clean numbers, reliable connectors, stable delivery, and reports clients can actually believe.\n\nThat is why measurement truth matters more than surface-level polish.\n\nIf the inputs are junk, the nicest report in the world is still junk.",
        'facebook': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nPretty dashboards are easy to love until the numbers stop making sense.\n\nFor agencies, trust comes from reporting that is stable, believable, and easy to deliver, not just visually tidy.",
        'x': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nA pretty dashboard does not create trust. Clean numbers, reliable connectors, and believable reporting do.",
        'youtube_title': 'DUMMY TEST - Pretty Dashboards Do Not Create Trust',
        'youtube_desc': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nThis placeholder YouTube upload supports a weekly dummy content run for Oviond.\n\nCore idea: pretty dashboards do not fix polluted inputs. Agencies trust reports when the numbers are believable and stable."
    },
    {
        'file': '2026-04-29-wednesday.json',
        'date': '2026-04-29T07:00:00.000Z',
        'tag': 'wednesday',
        'linkedin': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nFeature bloat is not a strategy.\n\nFor most agencies, the better product is the one that gets set up quickly, stays understandable, and does not need constant babysitting.\n\nSimple beats impressive when the job is monthly delivery, client trust, and team sanity.\n\nReporting software should lower admin load, not create more of it.",
        'facebook': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nSimple setup and low admin beat feature bloat more often than SaaS companies like to admit.\n\nAgencies need reporting tools they can trust without constant babysitting.",
        'x': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nFeature bloat is not a moat. For agencies, simple setup and low admin usually win.",
        'youtube_title': 'DUMMY TEST - Feature Bloat Is Not a Moat',
        'youtube_desc': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nThis placeholder YouTube upload supports a weekly dummy content run for Oviond.\n\nCore idea: simple setup and low admin beat feature bloat when agencies need reporting that actually gets delivered."
    },
    {
        'file': '2026-04-30-thursday.json',
        'date': '2026-04-30T07:00:00.000Z',
        'tag': 'thursday',
        'linkedin': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nAI can help agencies explain results faster.\n\nIt does not replace the harder operational layer: reliable connectors, clean delivery, permissions, scheduling, and client-ready trust.\n\nThe winning reporting product is not just an AI wrapper on top of charts.\n\nIt is a dependable operating system with AI helping where it actually matters.",
        'facebook': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nAI can help with explanation and speed.\n\nBut agencies still need the hard operational layer to work properly: connectors, delivery, permissions, and reliable reporting that clients can trust.",
        'x': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nAI can help explain results. It does not replace reliable connectors, stable delivery, and client-ready trust.",
        'youtube_title': 'DUMMY TEST - AI Helps, But It Does Not Replace the Ops Layer',
        'youtube_desc': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nThis placeholder YouTube upload supports a weekly dummy content run for Oviond.\n\nCore idea: AI should assist agency reporting, not replace the operational layer that makes reporting dependable."
    },
    {
        'file': '2026-05-01-friday.json',
        'date': '2026-05-01T07:00:00.000Z',
        'tag': 'friday',
        'linkedin': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nA lot of agency churn does not start with pricing.\nIt starts when the product feels fiddly, fragile, or too much work to trust.\n\nBetter reporting is not just about nicer charts.\nIt is about making delivery so simple and dependable that clients stop worrying and teams stop dreading month-end.\n\nThat is where real retention starts.",
        'facebook': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nRetention is not just a pricing story.\n\nWhen reporting feels fragile or high-maintenance, trust erodes fast. Agencies stay longer when delivery feels simple and dependable.",
        'x': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nA lot of churn starts before pricing becomes the argument. It starts when the product feels fiddly, fragile, or too much work to trust.",
        'youtube_title': 'DUMMY TEST - Retention Starts With Trust, Not Just Pricing',
        'youtube_desc': "DUMMY SCHEDULE TEST, REMOVE BEFORE PUBLISH\n\nThis placeholder YouTube upload supports a weekly dummy content run for Oviond.\n\nCore idea: retention improves when reporting feels simple, dependable, and low-friction, not just cheaper."
    }
]

for day in week:
    payload = {
        'type': 'schedule',
        'date': day['date'],
        'shortLink': False,
        'tags': ['oviond', 'dummy-test', day['tag']],
        'posts': [
            {
                'integration': {'id': linkedin},
                'value': [{'content': day['linkedin'], 'image': []}],
                'settings': {'__type': 'linkedin-page', 'post_as_images_carousel': False}
            },
            {
                'integration': {'id': facebook},
                'value': [{'content': day['facebook'], 'image': []}],
                'settings': {'__type': 'facebook'}
            },
            {
                'integration': {'id': x},
                'value': [{'content': day['x'], 'image': []}],
                'settings': {'__type': 'x', 'who_can_reply_post': 'everyone', 'made_with_ai': False, 'paid_partnership': False}
            },
            {
                'integration': {'id': youtube},
                'value': [{'content': day['youtube_desc'], 'image': [video]}],
                'settings': {
                    '__type': 'youtube',
                    'title': day['youtube_title'],
                    'type': 'unlisted',
                    'selfDeclaredMadeForKids': 'no',
                    'tags': [
                        {'value': 'oviond', 'label': 'oviond'},
                        {'value': 'agency reporting', 'label': 'agency reporting'},
                        {'value': 'dummy test', 'label': 'dummy test'}
                    ]
                }
            }
        ]
    }
    (out / day['file']).write_text(json.dumps(payload, indent=2), encoding='utf-8')

print(out)
