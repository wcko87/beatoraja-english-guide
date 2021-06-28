import os
import shutil

SOURCE = 'D:/bms/song/BOFXVI'
DEST = 'D:/bms/song/OUTPUT'

team_dirs = os.listdir(SOURCE)

def error(msg):
    print('ERROR: %s'%msg)
    quit()
        
print('> checking that all folders in SOURCE are dirs...')
for f in team_dirs:
    if not os.path.isdir(SOURCE + '/' + f):
        error('%s/%s is not a directory.' % (SOURCE,f))

all_song_dirs = []
song_dir_source = {}
print('> checking that all folders in team folders are dirs...')
for team_dir in team_dirs:
    path = SOURCE + '/' + team_dir
    team_songs = os.listdir(path)
    for team_song in team_songs:
        all_song_dirs.append(team_song)
        if team_song not in song_dir_source:
            song_dir_source[team_song] = [team_dir]
        else:
            song_dir_source[team_song].append(team_dir)
        if not os.path.isdir(path + '/' + team_song):
            error('%s/%s is not a directory.' % (path, team_song))

print('> checking that all song folder names are unique...')
if len(all_song_dirs) != len(set(all_song_dirs)):
    errors = ['duplicate song dirs detected! Please rename these song folders to make them unique.']
    for k, v in song_dir_source.items():
        if len(v) > 1:
            errors.append('Song folder "%s" in teams: %s' % (k,', '.join(v)))
    error('\n'.join(errors))

print('All Checks Passed. Copying song folders to destination folder...')

if True:
    try:
        os.makedirs(DEST)
    except:
        pass
    for team_dir in team_dirs:
        path = SOURCE + '/' + team_dir
        team_songs = os.listdir(path)
        for team_song in team_songs:
            path_from = path + '/' + team_song
            path_to = DEST + '/' + team_song
            print('Moving %s -> %s' % (path_from, path_to))
            shutil.move(path_from, path_to)

print('done')
