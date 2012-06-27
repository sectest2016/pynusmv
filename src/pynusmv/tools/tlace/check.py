from ...mc.mc import eval_ctl_spec
from .explain import explain

def check(fsm, spec):
    """
    Checks whether fsm satisfies spec and returns
    (True, None) if spec is satisfied,
    and (False, cntex) otherwise,
    where cntex is TLACE node explaining the violation.
    """
    
    initbdd = fsm.init
    specbdd = eval_ctl_spec(fsm, spec)
    
    # Get violating states
    violating = initbdd.compute_and(specbdd.compute_not())
    
    # If some initial states are not in specbdd, the spec if violated
    if violating.is_not_false():
        # Compute a counter-example
        enc = fsm.BddEnc
        state = enc.pick_one_state(violating)
        return (False, explain(fsm, state, spec))
        
    # Otherwise, it is satisfied
    else:
        return (True, None)    

            
class NuSMVCommandError(Exception):
    """An error occured during NuSMV command execution."""
    pass
