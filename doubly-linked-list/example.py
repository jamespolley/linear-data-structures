from MusicPlayer import MusicPlayer


# Create an empty MusicPlayer.
mp = MusicPlayer()

# Check if MusicPlayer can play a song.
mp.play()
print()

# Add songs.
mp.add('Wanted Dead or Alive', 'Bon Jovi', '5:08')
mp.add('Blaze of Glory', 'Bon Jovi', '5:42')
mp.add('Baby Come Back', 'Player', '4:19')
mp.add('Baby', 'Justin Bieber', '3:35')
mp.add('Dream On (Live)', 'Aerosmith', '4:27')
mp.add('Bohemian Rhapsody', 'Queen', '5:54')

# Print MusicPlayer library.
print(mp)

# # Print size of MusicPlayer.
print('Size of Library: ' + str(mp.get_size()) + ' songs' +'\n')

# Remove first song that completely matches 'Baby'.
mp.remove('Baby', partial_match=False)
print(mp)

# Play first song.
mp.play()

# Play next song.
mp.next()

# Edit song title.
mp.get_current_song().set_title('Dream On')
print()
print(mp)

# Play next songs. At end, start at beginning.
mp.next()
mp.next()
mp.next()
mp.next()

# Play previous song.
mp.prev()