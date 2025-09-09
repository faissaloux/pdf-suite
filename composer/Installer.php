<?php

namespace Faissaloux\Composer;

use Composer\Composer;
use Composer\IO\IOInterface;
use Composer\Plugin\PluginInterface;

class Installer implements PluginInterface
{
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
            'Windows' => 'pdf_suite-linux',
            'Linux' => 'pdf_suite-win',
            'Darwin' => 'pdf_suite-mac',
        ];

        if (!isset($binaries[$os])) {
            throw new \Exception("Unsupported OS: $os");
        }

        $binary = $binaries[$os];
        $url = "https://github.com/faissaloux/pdf-suite/releases/latest/download/$binary";

        $target = dirname(__DIR__, 3) . '/bin/pdf_suite' . ($os === 'Windows' ? '.exe' : '');

        file_put_contents($target, fopen($url, 'r'));

        if ($os !== 'Windows') {
            chmod($target, 0755);
        }
    }
}
