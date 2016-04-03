Vagrant.configure("2") do |config|
    config.vm.define 'web01' do |config|
        config.vm.box = 'ubuntu/trusty64'
        config.vm.hostname = 'web01'
        config.vm.synced_folder '.', '/vagrant', disabled: true
    end

    config.vm.define 'web02' do |config|
        config.vm.box = 'ubuntu/trusty64'
        config.vm.hostname = 'web02'
        config.vm.synced_folder '.', '/vagrant', disabled: true
    end
end
