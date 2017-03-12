# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: personaDefinition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='personaDefinition.proto',
  package='persona',
  syntax='proto3',
  serialized_pb=_b('\n\x17personaDefinition.proto\x12\x07persona\"\xf5\r\n\x07Persona\x12\"\n\x04\x44NAs\x18\x01 \x03(\x0b\x32\x14.persona.Persona.DNA\x12\x10\n\x08physical\x18\x02 \x01(\t\x12!\n\x03\x61ge\x18\x03 \x01(\x0b\x32\x14.persona.Persona.Age\x1a\x85\x0b\n\x03\x44NA\x12\x0b\n\x03\x44NA\x18\x01 \x01(\t\x12*\n\x06inputs\x18\x02 \x03(\x0b\x32\x1a.persona.Persona.DNA.Input\x12*\n\x06layers\x18\x03 \x03(\x0b\x32\x1a.persona.Persona.DNA.Layer\x12,\n\x07outputs\x18\x04 \x03(\x0b\x32\x1b.persona.Persona.DNA.Output\x12\x34\n\x0b\x63onnections\x18\x05 \x03(\x0b\x32\x1f.persona.Persona.DNA.Connection\x1a\x8d\x01\n\x05Input\x12\x16\n\x0einputLayerName\x18\x01 \x01(\t\x12\x36\n\x0einputTransform\x18\x03 \x01(\x0b\x32\x1e.persona.Persona.DNA.Transform\x12\x34\n\x0b\x63onnections\x18\x05 \x03(\x0b\x32\x1f.persona.Persona.DNA.Connection\x1a\xc9\x02\n\x05Layer\x12\x11\n\tlayerName\x18\x01 \x01(\t\x12,\n\tlayerSize\x18\x02 \x03(\x0b\x32\x19.persona.Persona.DNA.Size\x12\x34\n\x0b\x63onnections\x18\x03 \x03(\x0b\x32\x1f.persona.Persona.DNA.Connection\x12\x41\n\x10layerConvolution\x18\x04 \x01(\x0b\x32%.persona.Persona.DNA.LayerConvolutionH\x00\x12?\n\x0flayerActivation\x18\x05 \x01(\x0b\x32$.persona.Persona.DNA.LayerActivationH\x00\x12\x39\n\x0clayerDropout\x18\x06 \x01(\x0b\x32!.persona.Persona.DNA.LayerDropoutH\x00\x42\n\n\x08SubLayer\x1a}\n\x10LayerConvolution\x12\x1c\n\x14\x63onvolutionDimension\x18\x01 \x01(\x04\x12\x0f\n\x07\x66ilters\x18\x02 \x01(\x04\x12\x12\n\nkernelSize\x18\x03 \x03(\x04\x12\x12\n\nborderMode\x18\x04 \x01(\t\x12\x12\n\ninputShape\x18\x05 \x03(\x04\x1a)\n\x0fLayerActivation\x12\x16\n\x0e\x61\x63tivationType\x18\x01 \x01(\t\x1a&\n\x0cLayerDropout\x12\x16\n\x0e\x64ropPercentage\x18\x01 \x01(\x01\x1a\xa9\x01\n\x06Output\x12\x17\n\x0foutputLayerName\x18\x01 \x01(\t\x12\x17\n\x0foutputLayerType\x18\x02 \x01(\t\x12\x37\n\x0foutputTransform\x18\x03 \x01(\x0b\x32\x1e.persona.Persona.DNA.Transform\x12\x34\n\x0b\x63onnections\x18\x04 \x03(\x0b\x32\x1f.persona.Persona.DNA.Connection\x1a\xa7\x01\n\tTransform\x12\x17\n\x0ftransformerName\x18\x01 \x01(\t\x12\x17\n\x0finformationType\x18\x02 \x01(\t\x12\x30\n\rtransformSize\x18\x03 \x03(\x0b\x32\x19.persona.Persona.DNA.Size\x12\x36\n\x0etransformParam\x18\x04 \x03(\x0b\x32\x1e.persona.Persona.DNA.Parameter\x1a\x43\n\nConnection\x12\x17\n\x0fsourceLayerName\x18\x01 \x01(\t\x12\x1c\n\x14\x64\x65stinationLayerName\x18\x02 \x01(\t\x1a\x30\n\x04Size\x12\x11\n\tdimension\x18\x01 \x01(\x04\x12\x15\n\rdimensionSize\x18\x02 \x01(\x04\x1a:\n\tParameter\x12\x15\n\rparameterName\x18\x01 \x01(\t\x12\x16\n\x0eparameterValue\x18\x02 \x01(\t\x1a]\n\x03\x41ge\x12\x0b\n\x03old\x18\x01 \x01(\x04\x12\x15\n\rlearningCycle\x18\x02 \x01(\x04\x12\x32\n\x0c\x65nvironments\x18\x03 \x03(\x0b\x32\x1c.persona.Persona.Environment\x1a\xa9\x01\n\x0b\x45nvironment\x12>\n\x0cinformations\x18\x01 \x03(\x0b\x32(.persona.Persona.Environment.Information\x12\x0f\n\x07society\x18\x02 \x01(\t\x1aI\n\x0bInformation\x12\x19\n\x11informationSource\x18\x01 \x01(\t\x12\x1f\n\x17\x63onnectedInputLayerName\x18\x02 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERSONA_DNA_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='persona.Persona.DNA.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputLayerName', full_name='persona.Persona.DNA.Input.inputLayerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputTransform', full_name='persona.Persona.DNA.Input.inputTransform', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='persona.Persona.DNA.Input.connections', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=488,
)

_PERSONA_DNA_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='persona.Persona.DNA.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layerName', full_name='persona.Persona.DNA.Layer.layerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerSize', full_name='persona.Persona.DNA.Layer.layerSize', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='persona.Persona.DNA.Layer.connections', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerConvolution', full_name='persona.Persona.DNA.Layer.layerConvolution', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerActivation', full_name='persona.Persona.DNA.Layer.layerActivation', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerDropout', full_name='persona.Persona.DNA.Layer.layerDropout', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='SubLayer', full_name='persona.Persona.DNA.Layer.SubLayer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=491,
  serialized_end=820,
)

_PERSONA_DNA_LAYERCONVOLUTION = _descriptor.Descriptor(
  name='LayerConvolution',
  full_name='persona.Persona.DNA.LayerConvolution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convolutionDimension', full_name='persona.Persona.DNA.LayerConvolution.convolutionDimension', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters', full_name='persona.Persona.DNA.LayerConvolution.filters', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernelSize', full_name='persona.Persona.DNA.LayerConvolution.kernelSize', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='borderMode', full_name='persona.Persona.DNA.LayerConvolution.borderMode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputShape', full_name='persona.Persona.DNA.LayerConvolution.inputShape', index=4,
      number=5, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=947,
)

_PERSONA_DNA_LAYERACTIVATION = _descriptor.Descriptor(
  name='LayerActivation',
  full_name='persona.Persona.DNA.LayerActivation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activationType', full_name='persona.Persona.DNA.LayerActivation.activationType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=949,
  serialized_end=990,
)

_PERSONA_DNA_LAYERDROPOUT = _descriptor.Descriptor(
  name='LayerDropout',
  full_name='persona.Persona.DNA.LayerDropout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dropPercentage', full_name='persona.Persona.DNA.LayerDropout.dropPercentage', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=992,
  serialized_end=1030,
)

_PERSONA_DNA_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='persona.Persona.DNA.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputLayerName', full_name='persona.Persona.DNA.Output.outputLayerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputLayerType', full_name='persona.Persona.DNA.Output.outputLayerType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputTransform', full_name='persona.Persona.DNA.Output.outputTransform', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='persona.Persona.DNA.Output.connections', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1033,
  serialized_end=1202,
)

_PERSONA_DNA_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='persona.Persona.DNA.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transformerName', full_name='persona.Persona.DNA.Transform.transformerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='informationType', full_name='persona.Persona.DNA.Transform.informationType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transformSize', full_name='persona.Persona.DNA.Transform.transformSize', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transformParam', full_name='persona.Persona.DNA.Transform.transformParam', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1205,
  serialized_end=1372,
)

_PERSONA_DNA_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='persona.Persona.DNA.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceLayerName', full_name='persona.Persona.DNA.Connection.sourceLayerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destinationLayerName', full_name='persona.Persona.DNA.Connection.destinationLayerName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1374,
  serialized_end=1441,
)

_PERSONA_DNA_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='persona.Persona.DNA.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimension', full_name='persona.Persona.DNA.Size.dimension', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dimensionSize', full_name='persona.Persona.DNA.Size.dimensionSize', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1443,
  serialized_end=1491,
)

_PERSONA_DNA_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='persona.Persona.DNA.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameterName', full_name='persona.Persona.DNA.Parameter.parameterName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameterValue', full_name='persona.Persona.DNA.Parameter.parameterValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1493,
  serialized_end=1551,
)

_PERSONA_DNA = _descriptor.Descriptor(
  name='DNA',
  full_name='persona.Persona.DNA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DNA', full_name='persona.Persona.DNA.DNA', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='persona.Persona.DNA.inputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layers', full_name='persona.Persona.DNA.layers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='persona.Persona.DNA.outputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='persona.Persona.DNA.connections', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_DNA_INPUT, _PERSONA_DNA_LAYER, _PERSONA_DNA_LAYERCONVOLUTION, _PERSONA_DNA_LAYERACTIVATION, _PERSONA_DNA_LAYERDROPOUT, _PERSONA_DNA_OUTPUT, _PERSONA_DNA_TRANSFORM, _PERSONA_DNA_CONNECTION, _PERSONA_DNA_SIZE, _PERSONA_DNA_PARAMETER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=1551,
)

_PERSONA_AGE = _descriptor.Descriptor(
  name='Age',
  full_name='persona.Persona.Age',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old', full_name='persona.Persona.Age.old', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learningCycle', full_name='persona.Persona.Age.learningCycle', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='environments', full_name='persona.Persona.Age.environments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1553,
  serialized_end=1646,
)

_PERSONA_ENVIRONMENT_INFORMATION = _descriptor.Descriptor(
  name='Information',
  full_name='persona.Persona.Environment.Information',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='informationSource', full_name='persona.Persona.Environment.Information.informationSource', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connectedInputLayerName', full_name='persona.Persona.Environment.Information.connectedInputLayerName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1745,
  serialized_end=1818,
)

_PERSONA_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='persona.Persona.Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='informations', full_name='persona.Persona.Environment.informations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='society', full_name='persona.Persona.Environment.society', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_ENVIRONMENT_INFORMATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1649,
  serialized_end=1818,
)

_PERSONA = _descriptor.Descriptor(
  name='Persona',
  full_name='persona.Persona',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DNAs', full_name='persona.Persona.DNAs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physical', full_name='persona.Persona.physical', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age', full_name='persona.Persona.age', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_DNA, _PERSONA_AGE, _PERSONA_ENVIRONMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=1818,
)

_PERSONA_DNA_INPUT.fields_by_name['inputTransform'].message_type = _PERSONA_DNA_TRANSFORM
_PERSONA_DNA_INPUT.fields_by_name['connections'].message_type = _PERSONA_DNA_CONNECTION
_PERSONA_DNA_INPUT.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYER.fields_by_name['layerSize'].message_type = _PERSONA_DNA_SIZE
_PERSONA_DNA_LAYER.fields_by_name['connections'].message_type = _PERSONA_DNA_CONNECTION
_PERSONA_DNA_LAYER.fields_by_name['layerConvolution'].message_type = _PERSONA_DNA_LAYERCONVOLUTION
_PERSONA_DNA_LAYER.fields_by_name['layerActivation'].message_type = _PERSONA_DNA_LAYERACTIVATION
_PERSONA_DNA_LAYER.fields_by_name['layerDropout'].message_type = _PERSONA_DNA_LAYERDROPOUT
_PERSONA_DNA_LAYER.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYER.oneofs_by_name['SubLayer'].fields.append(
  _PERSONA_DNA_LAYER.fields_by_name['layerConvolution'])
_PERSONA_DNA_LAYER.fields_by_name['layerConvolution'].containing_oneof = _PERSONA_DNA_LAYER.oneofs_by_name['SubLayer']
_PERSONA_DNA_LAYER.oneofs_by_name['SubLayer'].fields.append(
  _PERSONA_DNA_LAYER.fields_by_name['layerActivation'])
_PERSONA_DNA_LAYER.fields_by_name['layerActivation'].containing_oneof = _PERSONA_DNA_LAYER.oneofs_by_name['SubLayer']
_PERSONA_DNA_LAYER.oneofs_by_name['SubLayer'].fields.append(
  _PERSONA_DNA_LAYER.fields_by_name['layerDropout'])
_PERSONA_DNA_LAYER.fields_by_name['layerDropout'].containing_oneof = _PERSONA_DNA_LAYER.oneofs_by_name['SubLayer']
_PERSONA_DNA_LAYERCONVOLUTION.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYERACTIVATION.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYERDROPOUT.containing_type = _PERSONA_DNA
_PERSONA_DNA_OUTPUT.fields_by_name['outputTransform'].message_type = _PERSONA_DNA_TRANSFORM
_PERSONA_DNA_OUTPUT.fields_by_name['connections'].message_type = _PERSONA_DNA_CONNECTION
_PERSONA_DNA_OUTPUT.containing_type = _PERSONA_DNA
_PERSONA_DNA_TRANSFORM.fields_by_name['transformSize'].message_type = _PERSONA_DNA_SIZE
_PERSONA_DNA_TRANSFORM.fields_by_name['transformParam'].message_type = _PERSONA_DNA_PARAMETER
_PERSONA_DNA_TRANSFORM.containing_type = _PERSONA_DNA
_PERSONA_DNA_CONNECTION.containing_type = _PERSONA_DNA
_PERSONA_DNA_SIZE.containing_type = _PERSONA_DNA
_PERSONA_DNA_PARAMETER.containing_type = _PERSONA_DNA
_PERSONA_DNA.fields_by_name['inputs'].message_type = _PERSONA_DNA_INPUT
_PERSONA_DNA.fields_by_name['layers'].message_type = _PERSONA_DNA_LAYER
_PERSONA_DNA.fields_by_name['outputs'].message_type = _PERSONA_DNA_OUTPUT
_PERSONA_DNA.fields_by_name['connections'].message_type = _PERSONA_DNA_CONNECTION
_PERSONA_DNA.containing_type = _PERSONA
_PERSONA_AGE.fields_by_name['environments'].message_type = _PERSONA_ENVIRONMENT
_PERSONA_AGE.containing_type = _PERSONA
_PERSONA_ENVIRONMENT_INFORMATION.containing_type = _PERSONA_ENVIRONMENT
_PERSONA_ENVIRONMENT.fields_by_name['informations'].message_type = _PERSONA_ENVIRONMENT_INFORMATION
_PERSONA_ENVIRONMENT.containing_type = _PERSONA
_PERSONA.fields_by_name['DNAs'].message_type = _PERSONA_DNA
_PERSONA.fields_by_name['age'].message_type = _PERSONA_AGE
DESCRIPTOR.message_types_by_name['Persona'] = _PERSONA

Persona = _reflection.GeneratedProtocolMessageType('Persona', (_message.Message,), dict(

  DNA = _reflection.GeneratedProtocolMessageType('DNA', (_message.Message,), dict(

    Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_INPUT,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Input)
      ))
    ,

    Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYER,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Layer)
      ))
    ,

    LayerConvolution = _reflection.GeneratedProtocolMessageType('LayerConvolution', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYERCONVOLUTION,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.LayerConvolution)
      ))
    ,

    LayerActivation = _reflection.GeneratedProtocolMessageType('LayerActivation', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYERACTIVATION,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.LayerActivation)
      ))
    ,

    LayerDropout = _reflection.GeneratedProtocolMessageType('LayerDropout', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYERDROPOUT,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.LayerDropout)
      ))
    ,

    Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_OUTPUT,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Output)
      ))
    ,

    Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_TRANSFORM,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Transform)
      ))
    ,

    Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_CONNECTION,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Connection)
      ))
    ,

    Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_SIZE,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Size)
      ))
    ,

    Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_PARAMETER,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Parameter)
      ))
    ,
    DESCRIPTOR = _PERSONA_DNA,
    __module__ = 'personaDefinition_pb2'
    # @@protoc_insertion_point(class_scope:persona.Persona.DNA)
    ))
  ,

  Age = _reflection.GeneratedProtocolMessageType('Age', (_message.Message,), dict(
    DESCRIPTOR = _PERSONA_AGE,
    __module__ = 'personaDefinition_pb2'
    # @@protoc_insertion_point(class_scope:persona.Persona.Age)
    ))
  ,

  Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), dict(

    Information = _reflection.GeneratedProtocolMessageType('Information', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_ENVIRONMENT_INFORMATION,
      __module__ = 'personaDefinition_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.Environment.Information)
      ))
    ,
    DESCRIPTOR = _PERSONA_ENVIRONMENT,
    __module__ = 'personaDefinition_pb2'
    # @@protoc_insertion_point(class_scope:persona.Persona.Environment)
    ))
  ,
  DESCRIPTOR = _PERSONA,
  __module__ = 'personaDefinition_pb2'
  # @@protoc_insertion_point(class_scope:persona.Persona)
  ))
_sym_db.RegisterMessage(Persona)
_sym_db.RegisterMessage(Persona.DNA)
_sym_db.RegisterMessage(Persona.DNA.Input)
_sym_db.RegisterMessage(Persona.DNA.Layer)
_sym_db.RegisterMessage(Persona.DNA.LayerConvolution)
_sym_db.RegisterMessage(Persona.DNA.LayerActivation)
_sym_db.RegisterMessage(Persona.DNA.LayerDropout)
_sym_db.RegisterMessage(Persona.DNA.Output)
_sym_db.RegisterMessage(Persona.DNA.Transform)
_sym_db.RegisterMessage(Persona.DNA.Connection)
_sym_db.RegisterMessage(Persona.DNA.Size)
_sym_db.RegisterMessage(Persona.DNA.Parameter)
_sym_db.RegisterMessage(Persona.Age)
_sym_db.RegisterMessage(Persona.Environment)
_sym_db.RegisterMessage(Persona.Environment.Information)


# @@protoc_insertion_point(module_scope)