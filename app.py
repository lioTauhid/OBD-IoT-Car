import obd

connection = obd.OBD()  # auto-connects to USB or RF port


def getCommandResponse(command):
    response = connection.query(command)
    return response.value


if __name__ == '__main__':
    speed = obd.commands.SPEED
    fuelStatus = obd.commands.FUEL_STATUS
    fuelType = obd.commands.FUEL_TYPE
    oilTemp = obd.commands.OIL_TEMP

    print(f"Vehicle Speed : {getCommandResponse(speed)}")
    print(f"Fuel System Status : {getCommandResponse(fuelStatus)}")
    print(f"Fuel Type : {getCommandResponse(fuelType)}")
    print(f"Engine oil temperature : {getCommandResponse(oilTemp)}")
