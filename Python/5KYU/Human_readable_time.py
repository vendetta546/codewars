def make_readable(seconds):
    s = str(seconds % 60).zfill(2)
    m = str((seconds // 60)%60).zfill(2)
    h = str((seconds // 3600)%100).zfill(2)
    return f"{h}:{m}:{s}"
