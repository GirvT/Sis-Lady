def roleAdd(ctx, role):
    user = ctx.author
    await user.add_roles(role)

def roleRemove(ctx, role):
    user = ctx.author
    await user.remove_roles(role)