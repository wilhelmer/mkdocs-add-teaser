from setuptools import setup, find_packages

setup(
    name='mkdocs-add-teaser',
    version='0.2.0',
    description='A MkDocs plugin to add a CSS class to the first paragraph after the first heading 1 in all pages of your project.',
    long_description='',
    keywords='mkdocs css',
    url='https://github.com/wilhelmer/mkdocs-add-teaser.git',
    author='Lars Wilhelmer',
    author_email='lars@wilhelmer.de',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-add-teaser = mkdocs_add_teaser_plugin.plugin:AddTeaserPlugin'
        ]
    }
)
