import turnkeyml.tools.export as export
import turnkeyml.tools.onnx as onnx_tools
import turnkeyml.common.plugins as plugins
import turnkeyml.tools.management_tools as mgmt
from turnkeyml.tools.discovery import Discover
import turnkeyml.tools.report as report

    # Plugin interface for sequences
    discovered_plugins = plugins.discover()

    # Populated supported sequences dict with builtin sequences
        mgmt.Version,
        mgmt.Cache,
        mgmt.ModelsLocation,
        report.Report,
        Discover,
        export.ExportPytorchModel,
        onnx_tools.OptimizeOnnxModel,
        onnx_tools.LoadOnnx,
        onnx_tools.ConvertOnnxToFp16,
        export.VerifyOnnxExporter,
    ]

    # Add sequences from plugins to supported sequences dict
    for module in discovered_plugins.values():
        if "tools" in module.implements.keys():
            for tool_class in module.implements["tools"]:
                    name = tool_class.__class__.unique_name
                    raise ValueError(
                        f"Your turnkeyml installation has two tools named '{name}' "
                        "installed. You must uninstall one of your plugins that includes "
                        f"This error was thrown while trying to import {module}"
                    )

