from setuptools import setup, find_packages

version = '4.0'

setup(name='Products.CMFPlone',
      version=version,
      description="The Plone Content Management System",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone CMF python Zope',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://plone.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.Archetypes',
          'Products.ATReferenceBrowserWidget',
          'Products.CMFActionIcons',
          'Products.CMFCalendar',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.CMFDynamicViewFTI',
          'Products.CMFFormController',
          'Products.CMFQuickInstallerTool',
          'Products.CMFTopic',
          'Products.CMFUid',
          'Products.DCWorkflow',
          'Products.ExtendedPathIndex',
          'Products.GenericSetup',
          'Products.MimetypesRegistry',
          'Products.PasswordResetTool',
          'Products.PlacelessTranslationService',
          'Products.PloneLanguageTool',
          'Products.PlonePAS',
          'Products.PluggableAuthService',
          'Products.PluginRegistry',
          'Products.PortalTransforms',
          'Products.ResourceRegistries',
          'Products.SecureMailHost',
          'Products.statusmessages',
          'archetypes.kss',
          'kss.core',
          'plone.app.contentmenu',
          'plone.app.content',
          'plone.app.contentrules',
          'plone.app.controlpanel',
          'plone.app.customerize',
          'plone.app.form',
          'plone.app.i18n',
          'plone.app.iterate',
          'plone.app.kss',
          'plone.app.layout',
          'plone.app.linkintegrity >=1.0.3',
          'plone.app.openid',
          'plone.app.portlets',
          'plone.app.redirector',
          'plone.app.viewletmanager',
          'plone.app.vocabularies',
          'plone.app.workflow',
          'plone.contentrules',
          'plone.fieldsets',
          'plone.i18n',
          'plone.intelligenttext',
          'plone.locking',
          'plone.memoize',
          'plone.openid',
          'plone.portlets',
          'plone.session',
          'plone.theme',
          'txtfilter',
          'wicked',
          'five.customerize',
          'five.localsitemanager',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
