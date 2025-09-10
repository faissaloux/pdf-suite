<?php

namespace Faissaloux\Composer;

use Composer\Composer;
use Composer\IO\IOInterface;
use Composer\Plugin\PluginInterface;

class Installer implements PluginInterface
{
    private string $repository = "faissaloux/pdf-suite";

    public function activate(Composer $composer, IOInterface $io)
    {
        $this->install();
    }

    public function deactivate(Composer $composer, IOInterface $io)
    {
        //
    }

    public function uninstall(Composer $composer, IOInterface $io)
    {
        //
    }

    private function install()
    {
        $os = PHP_OS_FAMILY;

        $binaries = [
            'Windows' => 'pdf_suite-win',
            'Linux' => 'pdf_suite-linux',
            'Darwin' => 'pdf_suite-mac',
        ];

        if (!isset($binaries[$os])) {
            throw new \Exception("Unsupported OS: $os");
        }

        $latestReleaseBinaries = $this->getLatestReleaseBinaries();
        $binary = $latestReleaseBinaries[$binaries[$os]];

        $target = dirname(__DIR__, 3) . '/bin/pdf_suite' . ($os === 'Windows' ? '.exe' : '');

        file_put_contents($target, fopen($binary, 'r'));

        if ($os !== 'Windows') {
            chmod($target, 0755);
        }
    }

    /**
     * @return array<string, string>
     */
    private function getLatestReleaseBinaries(): array
    {
        $url = "https://api.github.com/repos/{$this->repository}/releases";

        $opts = [
            "http" => [
                "header" => "User-Agent: pdf-suite\r\n"
            ]
        ];
        $context = stream_context_create($opts);
        $json = file_get_contents($url, false, $context);
        $releases = json_decode($json, true);

        $latestRelease = null;
        foreach ($releases as $release) {
            if ($release) {
                $latestRelease = $release;
                break; // Releases are sorted newest → oldest.
            }
        }

        if (!$latestRelease) {
            die("No release found.\n");
        }

        $assets = [];
        foreach ($latestRelease["assets"] as $asset) {
            $assets[$asset['name']] = $asset['browser_download_url'];
        }

        return $assets;
    }
}
