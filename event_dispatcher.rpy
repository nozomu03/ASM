







init -100 python:



    all_events = [ ]

















    class event(object):
        
        def __repr__(self):
            return '<event ' + self.name + '>'
        
        def __init__(self, name, *args, **kwargs):
            
            self.name = name
            
            exprs = [ ]
            
            for i in args:
                if isinstance(i, basestring):
                    exprs.append(event.evaluate(i))
                else:
                    exprs.append(i)
            
            self.exprs = exprs
            
            self.priority = kwargs.get('priority', 100)
            
            all_events.append(self)
        
        
        
        
        def check(self, valid):
            
            for i in self.exprs:
                if not i.eval(self.name, valid):
                    return False
            
            return True
        
        def properties(self):
            
            rv = { }
            
            for i in self.exprs:
                rv.update(i.properties())
            
            return rv
        
        
        
        class event_check(object):
            
            def properties(self):
                return { }
            
            def __invert__(self):
                return event.false(self)
            
            def __and__(self, other):
                return event.and_op(self, other)
            
            def __or__(self, other):
                return event.or_op(self, other)
        
        
        
        
        class evaluate(event_check):
            
            def __init__(self, expr):
                self.expr = expr
            
            def eval(self, name, valid):
                return eval(self.expr)
        
        
        
        class once(event_check):
            def eval(self, name, valid):
                return name not in events_executed
        
        
        
        
        class solo(event_check):
            def eval(self, name, valid):
                
                
                return not valid
        
        
        
        class only(solo):
            
            def properties(self):
                return dict(only=True)
        
        
        
        
        
        class happened(event_check):
            def __init__(self, *events):
                self.events = events
            
            def eval(self, name, valid):
                for i in self.events:
                    if i not in events_executed:
                        return False
                
                return True
        
        
        
        class random(event_check):
            
            def __init__(self, probability):
                self.probability = probability
            
            def eval(self, name, valid):
                return renpy.random.random() <= self.probability
        
        
        class choose_one(event_check):
            
            def __init__(self, group, group_count=1):
                self.group = group
                self.group_count = group_count
            
            def eval(self, name, valid):
                return True
            
            def properties(self):
                return dict(group=self.group,
                            group_count=self.group_count)
        
        
        
        
        class false(event_check):
            def __init__(self, cond):
                self.cond = cond
            
            def eval(self, name, valid):
                return not self.cond.eval(name, valid)
        
        
        class and_op(event_check):
            
            def __init__(self, *args):
                self.args = args
            
            def eval(self, name, valid):
                for i in self.args:
                    if not i.eval(name, valid):
                        return False
                return True
        
        
        class or_op(event_check):
            
            def __init__(self, *args):
                self.args = args
            
            def eval(self, name, valid):
                for i in self.args:
                    if i.eval(name, valid):
                        return True
                return False
        
        
        
        class depends(event_check):
            def __init__(self, *events):
                self.events = events
            
            def eval(self, name, valid):
                for i in self.events:
                    if i not in events_executed_yesterday:
                        return False
                
                return True



    skip_periods = 0




    def check_skip_period():
        
        global skip_periods
        
        if skip_periods:
            skip_periods -= 1
            return True
        else:
            return False

    def _m1_event_dispatcher__events_init():
        store.events_executed = { }
        store.events_executed_yesterday = { }

    config.start_callbacks.append(_m1_event_dispatcher__events_init)




label events_end_day:

    $ skip_periods = 0

    python hide:


        skip_periods = 0

        for k in events_executed:
            events_executed_yesterday[k] = True

    return



label events_run_period:

    $ events = [ ]

    python hide:

        eobjs = [ ]
        egroups = { }
        eingroup = { }

        for i in all_events:
            if not i.check(eobjs):
                continue
            
            eobjs.append(i)
            
            props = i.properties()
            
            if 'group' in props:
                group = props['group']
                count = props['group_count']
                
                egroups.setdefault(group, [ ]).extend([ i ] * count)
                eingroup[i] = group
            
            if 'only' in props:
                break

        echosen = { }

        for k in egroups:
            echosen[k] = renpy.random.choice(egroups[k])

        for i in eobjs:
            
            if i in eingroup and echosen[eingroup[i]] is not i:
                continue
            
            events.append(i.name)


    while not check_skip_period() and events:

        $ _event = events.pop(0)
        $ events_executed[_event] = True

        call expression _event from call_expression_event_1

    return



label events_end_period:

    $ skip_period = 1
    return




label events_skip_period:

    $ skip_period = 2
    return


init 100:
    python hide:

        all_events.sort(key=lambda i : i.priority)

    python hide:

        for i in all_events:
            if not renpy.has_label(i.name):
                raise Exception("'%s' is defined as an event somewhere in the game, but no label named '%s' was defined anywhere." % (i.name, i.name))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
