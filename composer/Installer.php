<?php

namespace Faissaloux\PDFSuite;

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
            'Windows' => 'pdf_suite-win.exe',
            'Linux' => 'pdf_suite-linux',
            'Darwin' => 'pdf_suite-mac',
        ];

        if (!isset($binaries[$os])) {
            throw new \Exception("Unsupported OS: $os");
        }

        $latestReleaseBinaries = $this->getLatestReleaseBinaries();
        $binary = $latestReleaseBinaries[$binaries[$os]];

        $targetDirectory = dirname(__DIR__, 3) . '/bin';
        if( !is_dir($targetDirectory)) {
            mkdir($targetDirectory);
        }

        $target = $targetDirectory . '/pdf_suite' . ($os === 'Windows' ? '.exe' : '');

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
        $tag = PDFSuite::VERSION;
        $url = "https://api.github.com/repos/{$this->repository}/releases/tags/v$tag";

        $opts = [
            "http" => [
                "header" => "User-Agent: pdf-suite\r\n"
            ]
        ];
        $context = stream_context_create($opts);

        $json = @file_get_contents($url, false, $context);

        if (!$json) {
            die("No release found.\n");
        }

        $release = json_decode($json, true);

        $assets = [];
        foreach ($release['assets'] as $asset) {
            $assets[$asset['name']] = $asset['browser_download_url'];
        }

        return $assets;
    }
}
