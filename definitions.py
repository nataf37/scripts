# coding=utf-8
image_source = "http://ikook.tlv.redhat.com/gen_images/cloud/CentOS-7-x86_64-GenericCloud.qcow2"
image_name = "CentOS-7-x86_64-GenericCloud.qcow2"
pipeline_file = "/etc/ceilometer/pipeline.yaml"
gnocchi_resources_file = "/etc/ceilometer/gnocchi_resources.yaml"
docker_file = "docker exec -ti"
docker_compute = "ceilometer_agent_compute"
docker_gnocchi="gnocchi_api"
ceilometer_conf =  "/etc/ceilometer/ceilometer.conf"

gnocchi_resources_input = '''
  - resource_type: generic
    metrics:
      - 'hardware.cpu.load.1min'
      - 'hardware.cpu.load.5min'
      - 'hardware.cpu.load.15min'
      '''
instance_values_assigned = ['hardware.cpu.load.1min','hardware.cpu.load.5min','hardware.cpu.load.15min']
instance_values_assigned_new = ['cpu','vcpus','disk.root.size']
instance_values_assigned_bug_coverage = ['disk.usage']
image_value_check = ['image.size']
instance_value_check = ['vcpus']
network_value_check=['network.create']
volume_value_check = ['volume.size']
mbm_measures = ['memory.bandwidth.total','memory.bandwidth.local']

aodh_alarm_list = ['threshold',
                   'event',
                   'composite',
                   'gnocchi_resources_threshold',
                   'gnocchi_aggregation_by_metrics_threshold',
                   'gnocchi_aggregation_by_resources_threshold']

alarm_out = 'combination'

aodh_process_list = ['aodh-listener','aodh-api','aodh-notifier','aodh-evaluator']
panko_process_list = ['panko-api']
gnocchi_process_list =  ['gnocchi-api', 'gnocchi-statsd', 'gnocchi-metricd']
ceilometer_process_list = ['ceilometer-notification','ceilometer-central']

gnocchi_pipeline_input='''
    - name: hw_source
      meters:
          - "hardware.cpu.load.1min"
          - "hardware.cpu.load.5min"
          - "hardware.cpu.load.15min"
      sinks:
          - meter_sink'''

gnocchi_pipeline_instance_input = '''
    - name: cpu_source
      meters:
          - "cpu"
      sinks:
          - cpu_sink
          - cpu_delta_sink
          - meter_sink'''

gnocchi_pipeline_image_input = '''
    - name: image_source
      meters:
          - 'image*'
      sinks:
          - meter_sink'''

gnocchi_pipeline_network_input = '''
    - name: image_source
      meters:
          - "network*"
      sinks:
          - meter_sink'''

gnocchi_pipeline_volume_input = '''
   - name: image_source
      meters:
          - "volume*"
      sinks:
          - meter_sink'''

gnocchi_resources_instance_input = """
 - resource_type: instance
    metrics:
      - 'instance'
      - 'memory'
      - 'memory.usage'
      - 'memory.resident'
      - 'vcpus'
      - 'cpu'
      - 'cpu_util'
      - 'cpu.delta'
      - 'disk.root.size'
      - 'disk.ephemeral.size'
      - 'disk.read.requests'
      - 'disk.read.requests.rate'
      - 'disk.write.requests'
      - 'disk.write.requests.rate'
      - 'disk.read.bytes'
      - 'disk.read.bytes.rate'
      - 'disk.write.bytes'
      - 'disk.write.bytes.rate'
      - 'disk.latency'
      - 'disk.iops'
      - 'disk.capacity'
      - 'disk.allocation'
      - 'disk.usage'
    attributes:
      host: resource_metadata.host
      image_ref: resource_metadata.image_ref_url
      display_name: resource_metadata.display_name
      flavor_id: resource_metadata.(instance_flavor_id|(flavor.id))
      server_group: resource_metadata.user_metadata.server_group
"""

gnocchi_resources_image_input = '''
  - resource_type: image
    metrics:
      - 'image'
      - 'image.size'
      - 'image.download'
      - 'image.serve'
    attributes:
      name: resource_metadata.name
      container_format: resource_metadata.container_format
      disk_format: resource_metadata.disk_format'''

gnocchi_resources_network_input = """
  - resource_type: network
    metrics:
      - 'bandwidth'
      - 'network'
      - 'network.create'
      - 'network.update'
      - 'subnet'
      - 'subnet.create'
      - 'subnet.update'
      - 'port'
      - 'port.create'
      - 'port.update'
      - 'router'
      - 'router.create'
      - 'router.update'
      - 'ip.floating'
      - 'ip.floating.create'
      - 'ip.floating.update'
      """
gnocchi_resources_volume_input = """
  - resource_type: volume
    metrics:
      - 'volume'
      - 'volume.size'
      - 'volume.create.start'
      - 'volume.create.end'
      - 'volume.delete.start'
      - 'volume.delete.end'
      - 'volume.update'
      - 'volume.resize.start'
      - 'volume.resize.end'
      - 'volume.attach.start'
      - 'volume.attach.end'
      - 'volume.detach.start'
      - 'volume.detach.end'
    attributes:
      display_name: resource_metadata.display_name
"""
proc_list = ["openstack-ceilometer-notification.service", "openstack-ceilometer-collector.service", "openstack-ceilometer-central.service"]
gnocchi_service_list = ["gnocchi-metricd", "gnocchi-statsd"]

archive_policy =  """ \
    -b '0' \
    -m mean \
    -m max \
    -m min \
    -m count \
    -d 'points:5,granularity:60' \
    -d 'granularity:300,timespan:900' \
    -d 'points:3,timespan:10800' """

archive_policy_check = ['points: 5, granularity: 0:01:00, timespan: 0:05:00',
'points: 3, granularity: 0:05:00, timespan: 0:15:00',
'points: 3, granularity: 1:00:00, timespan: 3:00:00']

archive_policy_name = "DeleteMeArchivePolicy"