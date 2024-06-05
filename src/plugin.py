class Plugin:
    def job_types(self) -> dict[str, dict]:
        plugin_version: str = getattr(self, 'plugin_manifest').version
        return {
            f'dockerfile:{plugin_version}': {
                'images': [
                    {
                        'source': 'job',
                        'dockerfile_path': 'Dockerfile',
                        'template': True,
                    },
                ],
            },
        }
