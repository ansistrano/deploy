Vagrant.configure("2") do |config|
    config.vm.define 'web01' do |config|
        config.vm.box = 'ubuntu/trusty64'
        config.vm.hostname = 'web01'
        config.vm.synced_folder '.', '/vagrant', disabled: true
        config.vm.network :forwarded_port, guest: 22, host: 2230, id: "ssh", auto_correct: false
    end

    config.vm.define 'web02' do |config|
        config.vm.box = 'ubuntu/trusty64'
        config.vm.hostname = 'web02'
        config.vm.synced_folder '.', '/vagrant', disabled: true
        config.vm.network :forwarded_port, guest: 22, host: 2231, id: "ssh", auto_correct: false
    end
end
