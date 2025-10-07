from html import *
import json

def make_page(*vargs):
    return html(
        head(
            meta(charset='UTF-8'),
            meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            meta(name='description', content='The home of some audio plugins and other tools for music production I\'ve made.'),

            link(rel='icon', href='res/logo.png', type='img/png'),
            meta(name='og:image', content='https://raw.githubusercontent.com/NotWoowoo/plugins/master/res/logo.png'),

            title('not_woowoo\'s audio_tools'),
            link(rel='stylesheet', href='styles.css'),
        ),
        body(
            *vargs
        ),
        lang="en"
    )

def make_nav():
    return nav(
        div(
            div(
                img(src='res/logo.png'),
                h3('not_woowoo\'s<br>audio_tools'),
                class_='nav-left'
            ),
            div(
                a('Plugins', href='#plugins'),
                a('About', href='#about'),
                class_='nav-right'
            ),
            class_='nav-content'
        )
    )

def make_hero():
    return section(
        div(
            div(
                h1('Hey, here are some audio plugins.'),
                p('I made these for fun, but perhaps you\'ll find them useful.'),
                class_='hero-text'
            ),
            '''
                <div class="mock-plugin">
                    <div class="plugin-window">
                        <div class="window-bar">not_plugin</div>
                        <div class="plugin-interface">
                            <div class="knobs">
                                <div class="knob"></div>
                                <div class="knob"></div>
                                <div class="knob"></div>
                            </div>
                            <div class="display">
                                <div class="waveform">
                                    <div class="wave-line"></div>
                                    <div class="wave-line"></div>
                                    <div class="wave-line"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            ''',
            class_='hero-content'
        ),
        class_='hero'
    )

def make_audio_player(title, src):
    return div(
        p(title),
        f'''
            <audio controls style="width: 400px;">
                <source src="{src}">
                Your browser does not support the audio element.
            </audio>
        ''',
        class_='audio-player'
    )

def make_plugin_step(name):
    return ''

def make_plugin_item(name, ver, desc, visual_img, demos, formats, platforms, download_url, src_url):
    return div(
        div(
            h2(name),
            div(f'{ver[0]} • v{ver[1]}', class_='plugin-version'),
            class_='plugin-header'
        ),
        div(
            div(
                div(desc, class_='plugin-desc-content'),
                # div(
                img(src=visual_img, class_='plugin-visual'),
                #     class_='plugin-visual'
                # ),
                class_='plugin-desc'
            ),
            div(
                h4('What Does it Sound Like?'),
                div(
                    elems(
                        div(
                            make_audio_player(name1, file1),
                            div('→', class_='chain-arrow'),
                            make_audio_player(name2, file2),
                            class_='audio-chain'
                        )
                        for name1, file1, name2, file2 in demos
                    ),
                    style='display: flex; gap: 1rem; flex-direction: column;'
                ),
                class_='audio-demo'
            ),
            class_='plugin-content'
        ),
        div(
            div(
                elems(span(f) for f in formats),
                span(class_='format-separator'),
                elems(span(p) for p in platforms),
                class_='plugin-formats'
            ),
            div(
                a('Download', href=download_url, class_='btn-download'),
                a('Source Code', href=src_url) if src_url else '',
                class_='plugin-download-btns'
            ),
            class_='plugin-download'
        ),
        class_='plugin-item'
    )

def make_installation(new_fmt):
    table = r'''
        <table border="0" style="width: 500px; text-align: center;">
          <thead>
            <tr>
              <th></th>
              <th>Windows</th>
              <th>Linux</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Clap</td>
              <td>C:\Program Files\Common Files\CLAP</td>
              <td>~/.clap</td>
            </tr>
            <tr>
              <td>VST3</td>
              <td>C:\Program Files\Common Files\VST3</td>
              <td>~/.vst3</td>
            </tr>
          </tbody>
        </table>
    ''' if new_fmt else elems(
        p('- Windows: C:/Program Files/Steinberg/VSTPlugins'),
        p('- Linux: not supported yet :(')
    )

    return div(
        p('<b>INSTALLATION</b> is quite easy.'),
        p('1. Click "Download."'),
        p('2. Download your preferred platform/format from the GitHub releases.') if new_fmt else '',
        p('3. Move the downloaded file to where your DAW scans for plugins:'),
        table,
        # p(r'- Clap on Windows: C:\Program Files\Common Files\CLAP'),
        # p(r'- VST3 on Windows: C:\Program Files\Common Files\VST3'),
        # p('- Clap on Linux: ~/.clap'),
        # p('- VST3 on Linux: ~/.vst3'),
        style='display: flex; gap: 0.5rem; flex-direction: column'
    )

def make_plugins():
    return section(
        div(
            make_plugin_item(
                'honey_comb',
                ('beta', '1.0'),
                elems(
                    p('This is a comb filter. Well... maybe not quite.'),
                    p('Modulate the delay time to hear a very weird effect that I can only think to describe as "viscous." This effect is caused by multiple delay times smoothly interpolating between values, causing the signal to interact with itself in strange ways.'),
                    p('Honey_comb can work as a regular delay or as a comb filter, but it\'s probably most interesting as a sound design tool.'),
                    p('Honey_comb Logo by', a('Deltalaiez', href='https://youtube.com/@deltalaiez')),
                    hr(),
                    make_installation(True)
                ),
                'res/hcomb.png',
                [
                    ('Ting noise', 'res/no_hcomb_ting.mp3', 'Honeycombed Ting Noise', 'res/hcomb_ting.mp3'),
                    ('Drum Loop', 'res/no_hcomb_drums.mp3', 'Honeycombed Drum loop', 'res/hcomb_drums.mp3')
                ],
                ['Clap', 'VST3'],
                ['Windows', 'Linux'],
                'https://github.com/NotWoowoo/honey-comb/releases/tag/v1.0',
                'https://github.com/NotWoowoo/honey-comb'
            ),
            make_plugin_item(
                'Digital Distortion',
                ('beta', '1.0'),
                elems(
                    p('It may only have one knob, but the one knob does something unique. This effect folds the wave onto itself in an interesting way that draws out noisy, metallic high-end timbres. This is purely a fun sound design tool.'),
                    p('I plan to re-make this plugin in the near future so that it supports more plugin formats and has more features. I\'ve also lost the source code, so any updates will need a rewrite either way.'),
                    hr(),
                    make_installation(False)
                ),
                'res/ddist.png',
                [
                    ('Sine Wave', 'res/no_ddist_sine.mp3', 'Distorted Sine Wave', 'res/ddist_sine.mp3'),
                    ('Saw Wave', 'res/no_ddist_saw.mp3', 'Distorted Saw Wave', 'res/ddist_saw.mp3'),
                    ('BASS', 'res/no_ddist_bass.mp3', 'Distorted BASS', 'res/ddist_bass.mp3')
                ],
                ['VST2'],
                ['Windows'],
                'res/DigitalDistortion.dll',
                ''
            ),
            class_='plugins-content'
        ),
        class_='plugins',
        id='plugins'
    )

def make_about():
    return section(
        div(
            h2('About These Plugins'),
            div(
            p('Hey there, I\'m not_woowoo! I made these plugins, because I like music production and programming. By combining the two, I hope to reach deeper into the space of sonic possibilities and push the boundaries of what’s possible in music. Plus, developing plugins is just a lot of fun. I’m sharing these tools so others can use them too, and, of course, it’d be awesome to see them used in action by others.'),
                p('Everything is free, but I\'m thinking of adding a "pay what you want (including free)" model at some point in the future.'),
                p('All plugins (that I haven\'t lost the code for) are open source. If you want to see how they work, modify them, report bugs, or help out, then feel free to check out the source code on GitHub.'),
                class_='about-text',
            ),
            div(
                div(
                    span('Built with:', class_='detail-label'),
                    span('C++ (but more C-like), CLAP, VST3'),
                    class_='detail'
                ),
                div(
                    span('Tested on:', class_='detail-label'),
                    span('FL Studio, Reaper, Ableton'),
                    class_='detail'
                ),
                div(
                    span('Platforms', class_='detail-label'),
                    span('Linux (X11), Windows. I\'ll support Mac one day...'),
                    class_='detail'
                ),
                class_='about-details'
            ),
            class_='about-content'
        ),
        class_='about',
        id='about'
    )

with open('index.html', 'w') as f:
    f.write(
        make_page(
            make_nav(),
            make_hero(),
            make_plugins(),
            make_about()
        )
    )
