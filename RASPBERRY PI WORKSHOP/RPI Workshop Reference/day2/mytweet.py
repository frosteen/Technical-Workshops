import twitter
api=twitter.Api(consumer_key='W5pOZZDRN3ZEfN6bDi7V1PFO0',
consumer_secret='QHemJAzRI5LIa2dyRryYswFUj1HwFZbxMzB1aFRpYTsjCeP0rU',
access_token_key='800572720152907776-mRSFZlWRemLdCA00QGgcgOo2IK27OnU',
access_token_secret='fzQMODTa59LT1V1NrUapK5tIPki1A3bR9ZyxdkGxjBJbv')
#print(api.VerifyCredentials())

status = api.PostUpdate('nice peter!')
print(status.text)

#statuses = api.GetUserTimeline(screen_name='RpiThinklab')
#print '\n'.join([s.text for s in statuses])

