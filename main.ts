bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
    basic.pause(1000)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Sad)
    basic.pause(1000)
})
// need bluetooth mouse service to be activated. (press A+B)
input.onButtonPressed(Button.A, function () {
    mouse.click()
    basic.showIcon(IconNames.Happy)
    basic.pause(100)
})
input.onButtonPressed(Button.AB, function () {
    // bluetooth mouse service activated
    mouse.startMouseService()
    basic.showLeds(`
        . # . . .
        . # # . .
        . # # # .
        . # # . .
        . . . # .
        `)
    basic.pause(1000)
})
let Pressure_sensor = 0
basic.showIcon(IconNames.Rollerskate)
basic.forever(function () {
    Pressure_sensor = pins.analogReadPin(AnalogPin.P0)
    if (Pressure_sensor > 10) {
        mouse.click()
        basic.showIcon(IconNames.Yes)
    } else {
        mouse.click()
        basic.showIcon(IconNames.Rollerskate)
    }
})
