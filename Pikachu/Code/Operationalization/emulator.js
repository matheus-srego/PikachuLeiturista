const awsIoT = require( 'aws-iot-device-sdk' );
const endpointFile = require( '/home/ec2-user/environment/endpoint.json' );
const deviceName = 'EnergyConsumption' // __dirname.split('/').pop();

const device = awsIoT.device({
   keyPath: '/home/ec2-user/environment/PikachuLeiturista/Pikachu/Code/Operationalization/private.pem.key',
  certPath: '/home/ec2-user/environment/PikachuLeiturista/Pikachu/Code/Operationalization/certificate.pem.crt',
    caPath: '/home/ec2-user/environment/root-emulator.crt',
  clientId: deviceName,
      host: endpointFile.endpointAddress
});

device.on( 'connect', function() {
    console.log('Connected to AWS IoT');
    
    infiniteLoopPublish();
});

function infiniteLoopPublish() 
{
    console.log('Sending Energy Consupmition telemetry data to AWS IoT for ' + deviceName);
    device.publish( "EnergyConsumption/telemetry", JSON.stringify( getCarData( deviceName ) ) );
    
    setTimeout( infiniteLoopPublish, 5000 );
}

function randomFloatBetween(minValue,maxValue){
    return parseFloat(Math.min(minValue + (Math.random() * (maxValue - minValue)),maxValue));
}

function getCarData(deviceName) {
    
    const data_energy = {
        'EnergyConsumption': {
            'datetime': new Date().toISOString().replace(/\..+/, ''),
            'C_temperature': randomFloatBetween(11.950139, 44.601062),
            'KW_use': randomFloatBetween(0.005924, 1.283848),
            'KW_home_office': randomFloatBetween(0.005924, 1.283848),
            'KW_living_room': randomFloatBetween(0.005924, 1.283848),
            'KW_kitchen': randomFloatBetween(0.005924, 1.283848),
            'KW_wine_cellar': randomFloatBetween(0.005924, 1.283848),
            'KW_barn': randomFloatBetween(0.005924, 1.283848),
            'KW_garage_door': randomFloatBetween(0.005924, 1.283848),
        }
    };
    
    let message = {};
    
    message['device'] = deviceName
    message['datetime'] = new Date().toISOString().replace(/\..+/, '');
    message['C_temperature'] = data_energy[deviceName].C_temperature;
    message['KW_use'] = data_energy[deviceName].KW_use;
    message['KW_home_office'] = data_energy[deviceName].KW_home_office;
    message['KW_living_room'] = data_energy[deviceName].KW_living_room;
    message['KW_kitchen'] = data_energy[deviceName].KW_kitchen;
    message['KW_wine_cellar'] = data_energy[deviceName].KW_wine_cellar;
    message['KW_barn'] = data_energy[deviceName].KW_barn;
    message['KW_garage_door'] = data_energy[deviceName].KW_garage_door;
    
    return message;
}