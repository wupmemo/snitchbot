import twint

# Configure
c = twint.Config()
c.Username = "potus"
c.Search = "great"

# Run
twint.run.Search(c)
