
async def onMessage(message, callback):
    await callback(message)
    await callback("Recieved")