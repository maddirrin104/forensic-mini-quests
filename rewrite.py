def callback(commit):
    if commit.author_email == b"buihieu195b@gmail.com":
        commit.author_email = b"hieubnc195@gmail.com"
        commit.committer_email = b"hieubnc195@gmail.com"