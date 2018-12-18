import optical_model as om
# from astropy import modeling

# Get the default model parameters to play with
pars = om.defaultParams('u7000')

# Let's see what the model says with the default parameters
print('{}'.format(
    om.evaluate_optical_model(1000, 1000, 1, 'u7000', 1, 1, pars)
))